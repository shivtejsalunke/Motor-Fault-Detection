"""Strict signal validation and deterministic fixed-window segmentation."""
from __future__ import annotations
from pathlib import Path
import csv
import numpy as np

REQUIRED_CSV_COLUMNS = {"signal", "label", "recording_id"}

def load_csv(path: str | Path) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Load long-form CSV fields signal,label,recording_id; reject malformed values."""
    signals, labels, groups = [], [], []
    with Path(path).open(newline="", encoding="utf-8") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames or not REQUIRED_CSV_COLUMNS.issubset(reader.fieldnames):
            raise ValueError(f"CSV requires columns: {sorted(REQUIRED_CSV_COLUMNS)}")
        for line, row in enumerate(reader, start=2):
            try:
                value = float(row["signal"])
            except (TypeError, ValueError) as exc:
                raise ValueError(f"invalid signal at line {line}") from exc
            if not np.isfinite(value):
                raise ValueError(f"non-finite signal at line {line}")
            if not row["label"] or not row["recording_id"]:
                raise ValueError(f"empty label/group at line {line}")
            signals.append(value)
            labels.append(row["label"])
            groups.append(row["recording_id"])
    if not signals:
        raise ValueError("CSV contains no samples")
    return np.asarray(signals, dtype=float), np.asarray(labels), np.asarray(groups)

def validate_signal(signal: np.ndarray, sampling_rate_hz: float) -> np.ndarray:
    x = np.asarray(signal, dtype=np.float64)
    if x.ndim != 1 or x.size < 2:
        raise ValueError("signal must be a 1-D array with at least 2 samples")
    if not np.isfinite(x).all():
        raise ValueError("signal must contain only finite values")
    if not np.isfinite(sampling_rate_hz) or sampling_rate_hz <= 0:
        raise ValueError("sampling rate must be positive and finite")
    return x

def segment_signal(signal: np.ndarray, window_samples: int, hop_samples: int | None = None) -> np.ndarray:
    x = np.asarray(signal, dtype=float)
    hop = window_samples if hop_samples is None else hop_samples
    if x.ndim != 1:
        raise ValueError("signal must be one-dimensional")
    if window_samples < 2 or hop < 1:
        raise ValueError("window_samples >= 2 and hop_samples >= 1 required")
    if x.size < window_samples:
        return np.empty((0, window_samples), dtype=float)
    return np.stack([x[start:start + window_samples]
                     for start in range(0, x.size - window_samples + 1, hop)])
