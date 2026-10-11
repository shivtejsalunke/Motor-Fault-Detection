import numpy as np
import pytest
from motor_fault_detection.data_loader import validate_signal, segment_signal
from motor_fault_detection.filtering import bandpass
from motor_fault_detection.preprocessing import remove_dc_and_normalize
from motor_fault_detection.features import extract_features, feature_matrix
from motor_fault_detection.fft_analysis import amplitude_spectrum
from motor_fault_detection.train import train_dataset

def test_validation_and_segmentation():
    x = np.arange(20.0)
    assert validate_signal(x, 1000).shape == (20,)
    assert segment_signal(x, 8, 4).shape == (4, 8)
    with pytest.raises(ValueError):
        validate_signal([1, np.nan], 100)

def test_bandpass_and_nyquist():
    x = np.sin(2 * np.pi * 100 * np.arange(2048) / 2000)
    filtered = bandpass(x, 2000, 20, 300)
    assert filtered.shape == x.shape and np.isfinite(filtered).all()
    with pytest.raises(ValueError):
        bandpass(x, 2000, 20, 1000)

def test_features_use_hz_axis():
    fs = 2048
    t = np.arange(2048) / fs
    x = np.sin(2 * np.pi * 128 * t)
    features = extract_features(x, fs)
    assert abs(features["dominant_frequency_hz"] - 128) <= 1
    frequency, amplitude = amplitude_spectrum(x, fs)
    assert frequency[np.argmax(amplitude)] == pytest.approx(128)
    matrix, names = feature_matrix(np.stack([x, x]), fs)
    assert matrix.shape[0] == 2 and "rms" in names

def test_normalize_constant():
    np.testing.assert_allclose(remove_dc_and_normalize(np.ones(8)), np.zeros(8))

def test_group_aware_training_and_metrics():
    rng = np.random.default_rng(17)
    fs, n = 1024, 256
    windows, labels, groups = [], [], []
    for group in range(12):
        label = "healthy" if group % 2 == 0 else "fault"
        tone = 70 if label == "healthy" else 190
        for _ in range(4):
            t = np.arange(n) / fs
            windows.append(np.sin(2 * np.pi * tone * t) + rng.normal(0, .06, n))
            labels.append(label)
            groups.append(f"recording-{group}")
    _, metrics = train_dataset(np.asarray(windows), np.asarray(labels), np.asarray(groups), fs, seed=3)
    assert "accuracy" in metrics and "confusion_matrix" in metrics
    assert set(metrics["train_groups"]).isdisjoint(metrics["test_groups"])

def test_training_requires_distinct_groups():
    with pytest.raises(ValueError):
        train_dataset(np.random.default_rng(2).normal(size=(8, 32)),
                      np.asarray(["a", "b"] * 4), np.asarray(["one"] * 8), 1000)
