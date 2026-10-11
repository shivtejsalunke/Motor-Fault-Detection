"""FFT amplitude-spectrum helper with frequency axis expressed in Hz."""
import numpy as np

def amplitude_spectrum(signal: np.ndarray, sampling_rate_hz: float) -> tuple[np.ndarray, np.ndarray]:
    x = np.asarray(signal, dtype=float)
    if x.ndim != 1 or x.size < 2 or not np.isfinite(x).all():
        raise ValueError("signal must be finite, 1-D, and length >= 2")
    if not np.isfinite(sampling_rate_hz) or sampling_rate_hz <= 0:
        raise ValueError("sampling rate must be positive and finite")
    window = np.hanning(x.size)
    amplitude = np.abs(np.fft.rfft((x - x.mean()) * window)) / max(window.sum(), np.finfo(float).eps)
    frequency_hz = np.fft.rfftfreq(x.size, d=1.0 / sampling_rate_hz)
    return frequency_hz, amplitude
