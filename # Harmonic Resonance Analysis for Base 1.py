# Harmonic Resonance Analysis for Base 10
# Author: Janique Tamisha Lawrence
# Date: March 2025
# Purpose: To analyze harmonic patterns and cyclic interdependencies in prime digits of π in base 10

import mpmath
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.stats import pearsonr

# Configuration
DIGIT_COUNT = 1000000  # Number of π digits to analyze
PRIME_DIGITS = {2, 3, 5, 7}  # Prime digits in base 10

# Generate π digits using mpmath
mpmath.mp.dps = DIGIT_COUNT + 10  # Set precision
pi_digits = str(mpmath.mp.pi)[2:]  # Get digits after '3.'

# Convert π digits to binary sequence (1 for prime, 0 for non-prime)
binary_sequence = [1 if int(digit) in PRIME_DIGITS else 0 for digit in pi_digits[:DIGIT_COUNT]]

# Fourier Transform to detect harmonic patterns
fft_values = np.abs(fft(binary_sequence))
fft_frequencies = fftfreq(len(binary_sequence))

# Normalize FFT values
normalized_fft = fft_values / np.max(fft_values)

# Binary Density Factor calculation
total_ones = sum(binary_sequence)
total_length = len(binary_sequence)
binary_density = total_ones / total_length

# Plotting FFT Spectrum
plt.figure(figsize=(10, 5))
plt.plot(fft_frequencies, normalized_fft)
plt.title('FFT Spectrum of Prime Digits in π (Base 10)')
plt.xlabel('Frequency')
plt.ylabel('Normalized Magnitude')
plt.grid(True)
plt.show()

# Print results
print(f"Binary Density Factor (BD): {binary_density:.6f}")
print(f"Max FFT Peak: {np.max(normalized_fft):.6f}")
