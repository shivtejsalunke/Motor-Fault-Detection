"""Train baseline classifiers using group-aware holdout evaluation."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GroupShuffleSplit
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score, precision_recall_fscore_support,
                             confusion_matrix, classification_report)
from .features import feature_matrix

def train_dataset(windows: np.ndarray, labels: np.ndarray, groups: np.ndarray,
                  sampling_rate_hz: float, model_type: str = "random_forest",
                  seed: int = 17, test_size: float = 0.25):
    windows, labels, groups = np.asarray(windows), np.asarray(labels), np.asarray(groups)
    if windows.ndim != 2 or len(windows) != len(labels) or len(groups) != len(labels):
        raise ValueError("expected windows [n, samples] and aligned labels/groups")
    if len(labels) < 4 or len(np.unique(labels)) < 2:
        raise ValueError("need at least four windows and two classes")
    if len(np.unique(groups)) < 2:
        raise ValueError("group-aware split needs at least two groups")
    if not 0 < test_size < 1:
        raise ValueError("test_size must be between 0 and 1")
    X, names = feature_matrix(windows, sampling_rate_hz)
    splitter = GroupShuffleSplit(n_splits=1, test_size=test_size, random_state=seed)
    train_idx, test_idx = next(splitter.split(X, labels, groups))
    if len(np.unique(labels[train_idx])) < 2:
        raise ValueError("training partition has fewer than two classes; adjust groups/split")
    if model_type == "random_forest":
        model = RandomForestClassifier(n_estimators=200, random_state=seed,
                                       class_weight="balanced", n_jobs=1)
    elif model_type == "logistic_regression":
        model = make_pipeline(StandardScaler(),
                              LogisticRegression(max_iter=2000, class_weight="balanced",
                                                 random_state=seed))
    else:
        raise ValueError("model_type must be random_forest or logistic_regression")
    model.fit(X[train_idx], labels[train_idx])
    prediction = model.predict(X[test_idx])
    label_order = sorted(np.unique(labels).tolist(), key=str)
    precision, recall, f1, _ = precision_recall_fscore_support(
        labels[test_idx], prediction, labels=label_order, average="macro", zero_division=0)
    metrics = {
        "split_method": "GroupShuffleSplit", "seed": seed,
        "n_windows": int(len(labels)), "n_train": int(len(train_idx)), "n_test": int(len(test_idx)),
        "train_groups": sorted(np.unique(groups[train_idx]).tolist()),
        "test_groups": sorted(np.unique(groups[test_idx]).tolist()),
        "features": names, "model_type": model_type,
        "accuracy": float(accuracy_score(labels[test_idx], prediction)),
        "macro_precision": float(precision), "macro_recall": float(recall), "macro_f1": float(f1),
        "class_labels": label_order,
        "confusion_matrix": confusion_matrix(labels[test_idx], prediction, labels=label_order).tolist(),
        "classification_report": classification_report(labels[test_idx], prediction, labels=label_order,
                                                        zero_division=0, output_dict=True),
    }
    return model, metrics

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dataset", type=Path, help="NPZ containing windows, labels and groups")
    parser.add_argument("--sampling-rate", type=float, required=True, help="documented sample rate in Hz")
    parser.add_argument("--model", choices=["random_forest", "logistic_regression"], default="random_forest")
    parser.add_argument("--seed", type=int, default=17)
    parser.add_argument("--out", type=Path, default=Path("results"))
    args = parser.parse_args()
    with np.load(args.dataset, allow_pickle=False) as archive:
        windows, labels, groups = archive["windows"], archive["labels"].astype(str), archive["groups"].astype(str)
    model, metrics = train_dataset(windows, labels, groups, args.sampling_rate, args.model, args.seed)
    args.out.mkdir(parents=True, exist_ok=True)
    import joblib
    joblib.dump(model, args.out / "model.joblib")
    (args.out / "metrics.json").write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    keys = ("accuracy", "macro_precision", "macro_recall", "macro_f1", "n_train", "n_test",
            "train_groups", "test_groups")
    print(json.dumps({key: metrics[key] for key in keys}, indent=2))

if __name__ == "__main__":
    main()
