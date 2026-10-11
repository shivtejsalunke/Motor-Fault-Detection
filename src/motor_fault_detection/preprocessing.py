"""Window-level DC removal and normalization helpers."""
import numpy as np

def remove_dc_and_normalize(window: np.ndarray, epsilon: float = 1e-12) -> np.ndarray:
    x = np.asarray(window, dtype=float)
    if x.ndim != 1 or x.size < 2 or not np.isfinite(x).all():
        raise ValueError("window must be finite, 1-D, and length >= 2")
    centered = x - np.mean(x)
    scale = np.sqrt(np.mean(centered ** 2))
    if scale <= epsilon:
        return np.zeros_like(centered)
    return centered / scale
