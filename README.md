# Motor Fault Detection
### Vibration Signal Processing · Condition Monitoring · Reproducible Evaluation

<div align="center">

[![MATLAB](https://img.shields.io/badge/MATLAB-App%20Designer-0076A8?style=for-the-badge)](https://www.mathworks.com/products/matlab.html)
[![DSP](https://img.shields.io/badge/DSP-FFT%20Analysis-6A1B9A?style=for-the-badge)](https://en.wikipedia.org/wiki/Fast_Fourier_transform)
[![Status](https://img.shields.io/badge/status-prototype%20%2F%20study-blue?style=for-the-badge)](#project-status)

</div>

## Project Status

**Stage:** [Specify the actual state: data-processing prototype / dashboard prototype / dataset evaluation / hardware-validated]  
**Last updated:** [YYYY-MM-DD]

Keep the description aligned with the actual implementation, dataset, and evidence. Distinguish real sensor measurements, public datasets, simulations, and generated examples.

## Problem Statement

This project explores a vibration-based motor condition-monitoring workflow. The pipeline inspects signals, computes documented signal features, and presents condition indicators through a dashboard. A warning indicator is not, by itself, proof of a mechanical failure.

## Objectives

- Inspect vibration data in the time and frequency domains.
- Extract documented signal features using FFT-based analysis.
- Present condition indicators and anomaly alerts in a MATLAB App Designer UI.
- Evaluate the method on a clearly described dataset or measurement setup.

## System Workflow

```text
Signal source
    ↓
Data validation and preprocessing
    ↓
Windowing and FFT / feature extraction
    ↓
Documented threshold or classifier logic
    ↓
Dashboard status indicator and event log
    ↓
Evaluation and plots
```

Add screenshots and a workflow diagram under `docs/images/`.

## Technology Stack

- MATLAB and MATLAB App Designer
- Digital signal processing / FFT
- [Actual classifier or threshold logic]
- [Actual sensor and microcontroller, if used]

## Repository Layout

Suggested structure — adapt it to the actual files:

```text
.
├── app/                 # App Designer file(s)
├── src/                 # Signal processing and condition logic
├── data/                # Dataset notes; respect licensing
├── tests/               # Unit/regression tests
├── results/
│   ├── figures/
│   └── metrics/
├── docs/
│   ├── images/
│   └── reports/
├── .gitignore
└── README.md
```

## Setup and Reproduction

Document the tested MATLAB release, required toolboxes, input-data format, sampling rate, signal units, and exact steps to open the app and reproduce the analysis.

1. Clone the repository.
2. Open MATLAB and set the repository as the working directory.
3. Add required source folders to the MATLAB path.
4. Load the documented dataset or example signal.
5. Run the analysis and compare outputs against included reference figures or logs.

Replace these generic steps with precise, verified instructions.

## Signal Processing Method

Explain the full method, including:
- Sampling frequency, sensor units, and signal calibration
- Detrending/filtering and handling of missing samples
- Window function and FFT length
- Amplitude normalization and frequency-axis calculation
- Features or frequency bands used for diagnosis
- Threshold/classifier selection and alert persistence rules

## Data & Evaluation

| Evaluation item | Documented value |
|---|---|
| Data source and license | [Fill in] |
| Motor type and operating conditions | [Fill in] |
| Fault classes / label definitions | [Fill in] |
| Number of recordings and windows | [Fill in] |
| Split strategy | [Fill in; avoid leakage between windows from the same recording] |
| Method used to infer condition | [Fill in] |
| Accuracy / precision / recall / F1 | [Measured value and calculation] |
| False alarm / missed detection rate | [Measured value] |

Previous project materials mention a 92% accuracy figure. Present this as a verified result only if the dataset, evaluation split, metric calculation, and supporting evidence are included. Accuracy alone may hide poor performance on rare fault classes.

## Results

Include representative time-series plots, spectra, dashboard screenshots, a confusion matrix where appropriate, and raw metric tables. Label each outcome as **measured**, **simulated**, or **estimated**.

## Limitations

- Results depend on sensor mounting, sample rate, operating conditions, and data quality.
- An anomaly alert is not a confirmed mechanical diagnosis.
- Document fault classes, load conditions, or sensors not tested.

## Roadmap

- [ ] Add dataset/source documentation and a reproducible example.
- [ ] Add tests for preprocessing and FFT features.
- [ ] Publish per-class metrics and false-alarm analysis.
- [ ] Add a dashboard demo and known-limitations section.

## Portfolio Documentation Guide

See [docs/PROJECT_PORTFOLIO_GUIDE.md](docs/PROJECT_PORTFOLIO_GUIDE.md) for a focused checklist of technical details and evidence to publish.

## References & License

Cite datasets, algorithms, MATLAB documentation, and relevant condition-monitoring references. Specify the actual repository license.

## Contact

**Shivtej Salunke · SAL Dynamics**  
[GitHub](https://github.com/shivtejsalunke) · [LinkedIn](https://www.linkedin.com/in/shivtejsalunke) · [Email](mailto:shivtejsalunke23@gmail.com)
