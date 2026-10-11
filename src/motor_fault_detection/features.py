"""Interpretable time- and frequency-domain features."""
import numpy as np
from scipy.stats import kurtosis, skew

def extract_features(window: np.ndarray, sampling_rate_hz: float) -> dict[str, float]:
    x = np.asarray(window, dtype=float)
    if x.ndim != 1 or x.size < 4 or not np.isfinite(x).all():
        raise ValueError("window must be finite, 1-D, and length >= 4")
    if not np.isfinite(sampling_rate_hz) or sampling_rate_hz <= 0:
        raise ValueError("sampling rate must be positive and finite")
    centered = x - np.mean(x)
    rms = float(np.sqrt(np.mean(centered ** 2)))
    peak = float(np.max(np.abs(centered)))
    spectrum = np.abs(np.fft.rfft(centered * np.hanning(x.size)))
    frequency_hz = np.fft.rfftfreq(x.size, d=1.0 / sampling_rate_hz)
    index = int(np.argmax(spectrum[1:]) + 1) if spectrum.size > 1 else 0
    total = float(np.sum(spectrum))
    centroid = float(np.sum(frequency_hz * spectrum) / total) if total > 0 else 0.0
    return {
        "mean": float(np.mean(x)), "std": float(np.std(x)), "rms": rms,
        "peak_to_peak": float(np.ptp(x)), "crest_factor": peak / rms if rms > 0 else 0.0,
        "kurtosis_excess": float(kurtosis(x, fisher=True, bias=False)) if np.std(x) > 0 else 0.0,
        "skewness": float(skew(x, bias=False)) if np.std(x) > 0 else 0.0,
        "dominant_frequency_hz": float(frequency_hz[index]),
        "spectral_centroid_hz": centroid,
    }

def feature_matrix(windows: np.ndarray, sampling_rate_hz: float,
                   feature_names: list[str] | None = None) -> tuple[np.ndarray, list[str]]:
    rows = [extract_features(window, sampling_rate_hz) for window in np.asarray(windows)]
    if not rows:
        raise ValueError("no windows provided")
    names = feature_names or list(rows[0].keys())
    unknown = set(names) - set(rows[0])
    if unknown:
        raise ValueError(f"unknown features: {sorted(unknown)}")
    return np.asarray([[row[name] for name in names] for row in rows]), names
