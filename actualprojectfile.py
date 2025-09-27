import matplotlib.pyplot as plt
import numpy as np

frequency = 2     
amplitude = 1
duration = 2       
sampling_rate = 1000


t = np.linspace(0, duration, int(sampling_rate * duration))


signal = amplitude * np.sin(2 * np.pi * frequency * t)


plt.figure(figsize=(10, 5))
plt.plot(t, signal, 'g-', linewidth=3)
plt.title(f'Sinusoidal Signal: {frequency} Hz, Amplitude: {amplitude}')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

print(f"Frequency: {frequency} Hz")
print(f"Amplitude: {amplitude}")
print(f"Duration: {duration} seconds")
print(f"Number of samples: {len(signal)}")