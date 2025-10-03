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

plt.figure(figsize=(15, 12))

plt.plot(t_sine, sine_wave)
plt.plot(t_sine_fast, sine_fast)
plt.plot(t_sine_slow, sine_slow)
plt.plot(t_sine, sine_wave,)
plt.plot(t_sine, shifted_sine)

plt.plot(t_sawtooth, sawtooth_wave)
plt.plot(t_sawtooth_fast, sawtooth_fast)
plt.plot(t_sawtooth_slow, sawtooth_slow)
plt.plot(t_sawtooth, sawtooth_wave)
plt.plot(t_sawtooth, shifted_sawtooth)



























