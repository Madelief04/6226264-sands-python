import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from signals import *

sine_wave = generate_sine_wave(2, 1, 2, 100)
sawtooth_wave = generate_sawtooth_wave(3, 0.4, 2, 100)


sine_fast = time_scale_signal(sine_wave, 2, 100)
sine_slow = time_scale_signal(sine_wave, 0.5, 100)

sawtooth_fast = time_scale_signal(sawtooth_wave, 2, 100)
sawtooth_slow = time_scale_signal(sawtooth_wave, 0.5, 100)

#time arrays for plotting
t_sine = np.linspace(0, 2, len(sine_wave))
t_sawtooth = np.linspace(0, 2, len(sawtooth_wave))

"""time arrays for original signals"""
shifted_sine = time_shift_signal(sine_wave, 1, 5)
shifted_sawtooth = time_shift_signal(sawtooth_wave, 3, 100)                                                                                 

"""time arrays for shifted signals"""   

#time arrays for scaled signals
t_sine_fast = np.linspace(0, 1, len(sine_fast))  
t_sine_slow = np.linspace(0, 4, len(sine_slow))  
t_sawtooth_fast = np.linspace(0, 1, len(sawtooth_fast))
t_sawtooth_slow = np.linspace(0, 4, len(sawtooth_slow))

"""time arrays for scaled signals"""

#plots
#normal sine wave
plt.figure(figsize=(8, 4))
plt.title('Original Sine Wave')
plt.plot(t_sine, sine_wave)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

"""normal sawtooth wave gets plotted here"""

#sine scaled faster
plt.figure(figsize=(8, 4))
plt.plot(t_sine_fast, sine_fast)
plt.title('Fast Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

""" sine wave scaled faster gets plotted here"""

#sine scaled slower
plt.figure(figsize=(8, 4))
plt.plot(t_sine_slow, sine_slow)
plt.title('Slow Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

"""sine wave scaled slower gets plotted here"""

#sine shifted
plt.figure(figsize=(8, 4))
plt.plot(t_sine, shifted_sine[0])
plt.title('Shifted Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

"""sine wave shifted gets plotted here"""

#sawtooth normal
plt.figure(figsize=(8, 4))
plt.plot(t_sawtooth, sawtooth_wave)
plt.title('Original Sawtooth Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

"""a normal sawtooth wave gets plotted here"""

#sawtooth scaled faster
plt.figure(figsize=(8, 4))
plt.plot(t_sawtooth_fast, sawtooth_fast)
plt.title('Fast Sawtooth Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

"""sawtooth wave scaled faster gets plotted here"""

#sawtooth scaled slower
plt.figure(figsize=(8, 4))
plt.plot(t_sawtooth_slow, sawtooth_slow)
plt.title('Slow Sawtooth Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()


"""sawtooth wave scaled slower gets plotted here"""

#sawtooth shifted
plt.figure(figsize=(8, 4))
plt.plot(t_sawtooth, shifted_sawtooth[0])
plt.title('Shifted Sawtooth Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

"""sawtooth wave shifted gets plotted here"""

























