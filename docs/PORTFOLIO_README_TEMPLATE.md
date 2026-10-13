# Predictive Maintenance Dashboard & Motor Fault Detection

> MATLAB/DSP project for inspecting vibration signals and presenting motor-condition indicators.

![MATLAB](https://img.shields.io/badge/MATLAB-App%20Designer-0076A8?style=flat-square)
![DSP](https://img.shields.io/badge/DSP-FFT%20Analysis-6A1B9A?style=flat-square)

## Project Status

**Stage:** [prototype / simulation / evaluated on dataset / hardware validated]  
**Last updated:** YYYY-MM-DD

Clearly distinguish implementation that exists today from planned work. Do not describe a simulated or dataset-only workflow as a validated industrial predictive-maintenance system.

## Problem & Approach

Describe the condition-monitoring problem, the signal source, and the main processing path. Explain which component performs feature extraction, which component produces a classification/alert, and what the dashboard displays.

## Workflow

1. Load or acquire vibration data.
2. Validate timestamps, sample rate, physical units, and missing data.
3. Apply documented preprocessing and windowing.
4. Compute FFT-derived features and apply the implemented detection method.
5. Render status indicators and log diagnostic events.

Add `docs/images/system-workflow.png` when an architecture diagram is available.

## Stack & Requirements

- MATLAB release: [tested version]
- App Designer: [version / included release]
- Toolboxes: [exact list]
- Data: [source, license, and format]
- Sensor/microcontroller: [exact part number, if used]

## Structure

```text
.
├── app/                 # MATLAB App Designer application
├── src/                 # Signal processing and detection functions
├── data/                # Dataset instructions; avoid unlicensed raw data
├── tests/               # Unit or regression tests
├── results/
│   ├── figures/
│   └── metrics/
├── docs/
│   ├── images/
│   └── reports/
└── README.md
```

## Setup & Run

Write the exact, tested steps needed to open the app, set paths, load sample data, and reproduce the analysis. Include commands or screenshots where useful.

## Signal Processing Method

Document sample rate, FFT size, window function, normalization, filtering, frequency bands, feature definitions, and decision thresholds. Explain why these choices are appropriate for the measured signal.

## Evaluation

| Item | Details |
|---|---|
| Data source and license | [fill in] |
| Operating conditions / labels | [fill in] |
| Number of recordings and windows | [fill in] |
| Split method | [fill in; avoid window-level leakage] |
| Detection/classification method | [fill in] |
| Metrics | [precision, recall, F1, confusion matrix, false-alarm rate] |

If a 92% accuracy number is used, include the exact held-out test protocol and calculation. Accuracy alone is not sufficient for imbalanced fault data.

## Results

Add reproducible plots, confusion matrix, representative spectra, and dashboard screenshots. Mark each outcome as measured, simulated, or estimated.

## Limitations & Roadmap

- [Known limitation]
- [Untested operating condition]
- [ ] Add repeatable sample-data preparation.
- [ ] Automate core signal-processing tests.
- [ ] Report per-class metrics and false-alarm rate.
- [ ] Capture an end-to-end app demonstration.

## References & License

Cite data sources, algorithms, relevant literature, and MATLAB documentation. Specify the project's actual license.

## Contact

**Shivtej Salunke · SAL Dynamics**  
[GitHub](https://github.com/shivtejsalunke) · [LinkedIn](https://www.linkedin.com/in/shivtejsalunke) · [Email](mailto:shivtejsalunke23@gmail.com)
