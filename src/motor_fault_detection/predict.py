"""Predict a class from one fixed-length CSV window."""
from pathlib import Path
import argparse, json, joblib
import numpy as np
from .features import feature_matrix

def predict_window(model_path: str | Path, signal: np.ndarray, sampling_rate_hz: float) -> dict:
    model = joblib.load(model_path)
    X, names = feature_matrix(np.asarray(signal, dtype=float).reshape(1, -1), sampling_rate_hz)
    label = model.predict(X)[0]
    confidence = float(np.max(model.predict_proba(X)[0])) if hasattr(model, "predict_proba") else None
    return {"label": str(label), "confidence": confidence, "features": names}

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("model", type=Path)
    parser.add_argument("signal_csv", type=Path, help="one window as comma-separated numeric samples")
    parser.add_argument("--sampling-rate", type=float, required=True)
    args = parser.parse_args()
    signal = np.loadtxt(args.signal_csv, delimiter=",")
    print(json.dumps(predict_window(args.model, signal, args.sampling_rate), indent=2))

if __name__ == "__main__":
    main()
