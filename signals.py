import matplotlib.pyplot as plt
import numpy as np


def generate_sine_wave (frequency, amplitude, duration, sampling_rate): 
    t = np.linspace(0, duration, int(sampling_rate * duration))
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    return signal

sine_wave = generate_sine_wave (2, 1, 2, 100)

print (sine_wave)
plt.plot(sine_wave)