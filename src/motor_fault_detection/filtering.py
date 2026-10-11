"""Butterworth band-pass helper with explicit Nyquist validation."""
import numpy as np
from scipy.signal import butter, sosfiltfilt

def bandpass(signal: np.ndarray, sampling_rate_hz: float, low_hz: float,
             high_hz: float, order: int = 4) -> np.ndarray:
    x = np.asarray(signal, dtype=float)
    if x.ndim != 1 or x.size < 2 or not np.isfinite(x).all():
        raise ValueError("signal must be finite, 1-D, and length >= 2")
    if not np.isfinite(sampling_rate_hz) or sampling_rate_hz <= 0:
        raise ValueError("sampling rate must be positive and finite")
    if not 0 < low_hz < high_hz < sampling_rate_hz / 2:
        raise ValueError("require 0 < low_hz < high_hz < sampling_rate_hz/2")
    if order < 1:
        raise ValueError("order must be >= 1")
    sos = butter(order, [low_hz, high_hz], btype="bandpass",
                 fs=sampling_rate_hz, output="sos")
    try:
        return sosfiltfilt(sos, x)
    except ValueError as exc:
        raise ValueError("signal is too short for zero-phase filtering") from exc
