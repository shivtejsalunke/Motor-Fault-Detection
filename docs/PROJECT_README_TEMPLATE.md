# Predictive Maintenance Dashboard & Motor Fault Detection

> MATLAB-based vibration-analysis and motor-condition monitoring project.

![MATLAB](https://img.shields.io/badge/MATLAB-App%20Designer-0076A8?style=flat-square)
![DSP](https://img.shields.io/badge/DSP-FFT%20Analysis-6A1B9A?style=flat-square)
![Status](https://img.shields.io/badge/status-in%20development-orange?style=flat-square)

## Overview

This project explores a workflow for processing vibration signals and presenting motor-condition information in a MATLAB App Designer dashboard. The intended workflow includes signal parsing, FFT-based inspection, a visual status indicator, and anomaly alerts.

**Important:** document whether results come from real motor measurements, a public dataset, simulation, or generated test data. A reported 92% accuracy figure should only be published with its dataset, split strategy, evaluation metric, and repeatable calculation.

## Objectives

- Parse vibration data and inspect its frequency-domain characteristics.
- Present diagnostic status in a usable dashboard.
- Generate alerts from explicitly documented decision logic.
- Evaluate detection quality and failure modes using a reproducible test set.

## System Workflow

1. Acquire or load vibration samples.
2. Validate sample rate, units, timestamps, and missing values.
3. Apply documented preprocessing and windowing.
4. Compute FFT/features and apply a documented decision or classification method.
5. Display the result and preserve logs for later review.

Add a diagram to `docs/images/system-workflow.png` when available.

## Technology

- MATLAB
- MATLAB App Designer
- FFT / digital signal processing
- [Classifier or threshold logic — specify actual method]
- [Sensor / microcontroller setup — specify exact hardware if used]

## Repository Layout

```text
.
├── app/
│   └── MotorFaultDashboard.mlapp
├── src/
│   ├── load_vibration_data.m
│   ├── preprocess_signal.m
│   ├── compute_fft_features.m
│   └── classify_condition.m
├── data/
│   └── README.md
├── tests/
│   └── test_signal_processing.m
├── results/
│   ├── figures/
│   └── metrics/
├── docs/
│   ├── images/
│   └── reports/
├── .gitignore
└── README.md
```

Rename example files to match the actual implementation. Do not commit private, confidential, or unlicensed data.

## Requirements

- MATLAB version: [tested version]
- Toolboxes: [list exact required toolboxes]
- Data: [source, license, sample rate, units, labels]
- Hardware: [exact sensor, microcontroller, and motor setup, or “not required”]

## Setup & Run

1. Clone this repository.
2. Open MATLAB and set the repository root as the current folder.
3. Add the source directory to the MATLAB path.
4. Open the App Designer app and load the documented sample dataset.
5. Run the analysis and compare outputs to the included reference results.

Provide exact commands and the tested MATLAB release before considering the project reproducible.

## Signal Processing Method

Document the sample frequency, FFT length, window function, normalization, filtering, feature definitions, and any frequency bands used.

```matlab
% Illustrative example only — adapt to the actual sample format and method.
x = double(vibrationSignal(:));
x = x - mean(x);
N = numel(x);
X = fft(x);
amplitude = abs(X / N);
```

Explain how the production analysis differs from this illustrative snippet.

## Evaluation

| Item | Value |
|---|---|
| Data source and license | [Fill in] |
| Number of samples / windows | [Fill in] |
| Label definitions | [Fill in] |
| Train / validation / test split | [Fill in, if applicable] |
| Classification or alert method | [Fill in] |
| Accuracy / precision / recall / F1 | [Report measured values] |
| False alarm and missed detection rate | [Report measured values] |

If you report 92% accuracy, state the exact denominator and test protocol and include a confusion matrix. Avoid leakage between overlapping windows from the same recording.

## Limitations

- Performance depends on sensor placement, sample rate, motor operating conditions, and data quality.
- An alert is not by itself proof of a mechanical failure.
- Document untested fault types and operating regimes.

## Roadmap

- [ ] Add a documented sample dataset or data-generation script.
- [ ] Add automated tests for FFT feature extraction.
- [ ] Include confusion matrix and per-class metrics.
- [ ] Capture a dashboard demo and explain alert thresholds.

## References

Add references to the data source, relevant motor diagnostics material, MATLAB documentation, and any algorithms used.

## Contact

**Shivtej Salunke · SAL Dynamics**  
[GitHub](https://github.com/shivtejsalunke) · [LinkedIn](https://www.linkedin.com/in/shivtejsalunke) · [Email](mailto:shivtejsalunke23@gmail.com)
