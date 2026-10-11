# Evaluation protocol

1. Obtain and document a legitimate dataset and define labels before modeling.
2. Preserve recording/session/machine identifiers through segmentation.
3. Split by group using `GroupShuffleSplit`; overlapping windows from the same group must never appear in both partitions.
4. Train the fixed-seed Random Forest baseline or Logistic Regression alternative.
5. Report accuracy, macro precision, macro recall, macro F1, class-wise scores and a labeled confusion matrix. Macro metrics give classes equal weight; accuracy alone may hide poor minority-class recall.
6. Repeat across predeclared group splits or use grouped cross-validation for more reliable uncertainty estimates.
7. Save dataset version/checksum, dependency environment, configuration, seed, grouping identifiers, model and JSON metrics.
8. Preserve an untouched test machine/session when possible and report false-negative/false-alarm trade-offs for the intended application.

Automated tests use synthetic sinusoids to validate software behavior. Their score must not be described as measured motor-fault accuracy.
