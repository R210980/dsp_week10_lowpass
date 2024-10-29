import numpy as np
import matplotlib.pyplot as plt

# Take input from the user
fs = float(input("Enter the sampling frequency (Hz): "))
npoint = int(input("Enter the number of points (npoint): "))
cutoff_freq = float(input("Enter the cutoff frequency (Hz): "))

# Frequency resolution and Nyquist frequency
nyquist = fs / 2
freqs = np.linspace(0, nyquist, npoint // 2)

# Create the ideal low-pass filter response H(k)
H = np.zeros(npoint // 2)
H[freqs <= cutoff_freq] = 1  # Set gain = 1 for frequencies below cutoff

# Plot the magnitude response
plt.figure(figsize=(10, 5))
plt.plot(freqs, H, label=f'Low-pass filter (cutoff = {cutoff_freq} Hz)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('|H(k)|')
plt.title('Ideal Low-Pass Filter Response')
plt.grid(True)
plt.legend()
plt.show()
