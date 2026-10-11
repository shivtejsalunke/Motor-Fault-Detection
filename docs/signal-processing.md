# Signal-processing choices

- Sampling frequency is supplied explicitly in Hz and validated as positive.
- Optional Butterworth band-pass filtering validates `0 < low < high < fs/2` and uses second-order sections with forward/backward filtering.
- Windows are segmented using explicit sample-count window and hop lengths. Overlap creates correlated samples, so evaluation uses recording/session groups rather than random window splits.
- Time features include mean, standard deviation, RMS after DC removal, peak-to-peak, crest factor, excess kurtosis and skewness.
- Frequency analysis uses `rfft` and `rfftfreq(..., d=1/fs)`, a Hann window, dominant non-DC frequency and magnitude-weighted spectral centroid.

Feature units depend on sensor calibration; frequency features are Hz. Any filter, normalization or scaling used during training must be reproduced in inference. Zero-phase filtering is an offline operation and must not be described as a causal real-time filter.
