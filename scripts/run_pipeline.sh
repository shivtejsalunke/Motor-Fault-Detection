#!/usr/bin/env bash
set -euo pipefail
if [[ $# -lt 2 ]]; then
  echo "Usage: bash scripts/run_pipeline.sh DATASET.npz SAMPLING_RATE_HZ [output-dir]" >&2
  exit 2
fi
DATASET=$1
RATE=$2
OUT=${3:-results}
PYTHONPATH="src${PYTHONPATH:+:$PYTHONPATH}" python -m motor_fault_detection.train "$DATASET" --sampling-rate "$RATE" --out "$OUT"
