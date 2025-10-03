import matplotlib.pyplot as plt
import numpy as np
from scipy import signal




#time arrays for plotting
t_sine = np.linspace(0, 2, len(sine_wave))
t_sawtooth = np.linspace(0, 2, len(sawtooth_wave))

#time arrays for scaled signals
t_sine_fast = np.linspace(0, 1, len(sine_fast))  
t_sine_slow = np.linspace(0, 4, len(sine_slow))  
t_sawtooth_fast = np.linspace(0, 1, len(sawtooth_fast))
t_sawtooth_slow = np.linspace(0, 4, len(sawtooth_slow))

#time arrays for plotting
plt.figure(figsize=(8, 4))

plt.title('Original Sine Wave')
plt.plot(t_sine, sine_wave)
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(t_sine_fast, sine_fast)
plt.title('Fast Sine Wave')
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(t_sine_slow, sine_slow)
plt.title('Slow Sine Wave')
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(t_sine, shifted_sine)
plt.title('Shifted Sine Wave')
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(t_sawtooth, sawtooth_wave)
plt.title('Original Sawtooth Wave')
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(t_sawtooth_fast, sawtooth_fast)
plt.title('Fast Sawtooth Wave')
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(t_sawtooth_slow, sawtooth_slow)
plt.title('Slow Sawtooth Wave')
plt.show()

plt.figure(figsize=(8, 4))
plt.plot(t_sawtooth, shifted_sawtooth)
plt.title('Shifted Sawtooth Wave')
plt.show()



























