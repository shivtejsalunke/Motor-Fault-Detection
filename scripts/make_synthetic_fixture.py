#!/usr/bin/env python3
"""Create a synthetic-only vibration dataset for a software smoke test."""
import argparse
from pathlib import Path
import numpy as np

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    rng = np.random.default_rng(17)
    fs, n = 1024, 256
    windows, labels, groups = [], [], []
    for group in range(16):
        label = "healthy" if group % 2 == 0 else "fault"
        tone_hz = 70 if label == "healthy" else 190
        for _ in range(5):
            t = np.arange(n) / fs
            windows.append(np.sin(2 * np.pi * tone_hz * t) + rng.normal(0, 0.05, n))
            labels.append(label)
            groups.append(f"synthetic-recording-{group}")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(args.out, windows=np.asarray(windows),
                        labels=np.asarray(labels), groups=np.asarray(groups))
    print(f"Wrote SYNTHETIC-only fixture: {args.out} ({len(windows)} windows)")

if __name__ == "__main__":
    main()
