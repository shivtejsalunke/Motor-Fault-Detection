# Dataset policy and input schema

No public benchmark dataset is bundled or represented as downloaded in this repository. Before using measurements, verify source provenance, access terms/license, sample rate, units, machine/recording IDs, operating conditions and class labels; record the details in [docs/dataset-card.md](../docs/dataset-card.md).

Training expects an NPZ archive containing:

- `windows`: numeric array shaped `[number_of_windows, samples_per_window]`.
- `labels`: one string label per window.
- `groups`: recording/session/machine ID per window. Groups drive the held-out split.

All arrays must align on their first dimension. Sampling rate must come from acquisition records and is supplied explicitly in Hz. Signal units depend on sensor calibration and scaling. Do not split overlapping windows from one physical trace across training and test partitions.

Tests use generated signals strictly as **synthetic software fixtures**, not machine measurements. Do not commit proprietary or large datasets without confirming redistribution rights.
