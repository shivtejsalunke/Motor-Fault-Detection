"""Evaluate a serialized model on a separate NPZ dataset of labelled windows."""
from pathlib import Path
import argparse, json, joblib
import numpy as np
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, confusion_matrix
from .features import feature_matrix

def evaluate(model_path: str | Path, dataset_path: str | Path, sampling_rate_hz: float) -> dict:
    model = joblib.load(model_path)
    with np.load(dataset_path, allow_pickle=False) as archive:
        windows, labels = archive["windows"], archive["labels"].astype(str)
    X, names = feature_matrix(windows, sampling_rate_hz)
    prediction = model.predict(X)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, prediction,
                                                               average="macro", zero_division=0)
    label_order = sorted(set(labels.tolist()) | set(prediction.tolist()))
    return {"accuracy": float(accuracy_score(labels, prediction)),
            "macro_precision": float(precision), "macro_recall": float(recall),
            "macro_f1": float(f1), "class_labels": label_order,
            "confusion_matrix": confusion_matrix(labels, prediction, labels=label_order).tolist(),
            "features": names, "dataset": str(dataset_path), "model": str(model_path)}

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("model", type=Path)
    parser.add_argument("dataset", type=Path)
    parser.add_argument("--sampling-rate", type=float, required=True)
    parser.add_argument("--out", type=Path, default=Path("results/evaluation.json"))
    args = parser.parse_args()
    result = evaluate(args.model, args.dataset, args.sampling_rate)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
