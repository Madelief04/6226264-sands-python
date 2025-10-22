import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# sine wave with parameters frequency, amplitude, duration, sampling_rate
def generate_sine_wave (frequency, amplitude, duration, sampling_rate): 
    t = np.linspace(0, duration, int(sampling_rate * duration))
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    return signal

sine_wave = generate_sine_wave (2, 1, 2, 5)

""""generate a sine wave signal using the parameters frequency, amplitude, duration, and sampling_rate.
The function returns a numpy array representing the sine wave signal. """           

# sawtooth wave with parameters frequency, amplitude, duration, sampling_rate, width =1
def generate_sawtooth_wave (frequency, amplitude, duration, sampling_rate, width =1 ): 
    t = np.linspace(0, duration, int(sampling_rate * duration))
    sawtooth_wave = amplitude * signal.sawtooth(2 * np.pi * frequency * t, width)
    return sawtooth_wave



sawtooth_wave = generate_sawtooth_wave (3, 0.4, 2, 100)

"""a sawtooth wave signal using the parameters frequency, amplitude, duration, sampling_rate, and width is generated. 
The function returns a numpy array representing the sawtooth wave signal."""

#function for time shift
def time_shift_signal(signal, shift_seconds, sampling_rate):
    shift_samples = int(shift_seconds * sampling_rate)
    return (signal, shift_samples)

sine_shifted = time_shift_signal(sine_wave, 1, 5) 
sawtooth_shifted = time_shift_signal(sawtooth_wave, 3, 100)  

""""shift a signal in time by a specified number of seconds. The function takes a signal (numpy array), shift in seconds, and sampling rate as inputs.
It returns the shifted signal as a numpy array. """


#function for time scaling
def time_scale_signal(signal, scale_factor, sampling_rate):
    original_length = len(signal)
    new_length = int(original_length / scale_factor)
    
    original_indices = np.arange(original_length)
    new_indices = np.linspace(0, original_length - 0.05, new_length)
    
    scaled_signal = np.interp(new_indices, original_indices, signal)
    return scaled_signal

sine_fast = time_scale_signal(sine_wave, 2, 100)
sine_slow = time_scale_signal(sine_wave, 0.5, 100)

sawtooth_fast = time_scale_signal(sawtooth_wave, 2, 100)
sawtooth_slow = time_scale_signal(sawtooth_wave, 0.5, 100)

""""time scale a signal by a specified factor. The function takes a signal (numpy array), scale factor, and sampling rate as inputs.
It returns the time-scaled signal as a numpy array. """ 

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

""" """

#sine scaled slower
plt.figure(figsize=(8, 4))
plt.plot(t_sine_slow, sine_slow)
plt.title('Slow Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

#sine shifted
plt.figure(figsize=(8, 4))
plt.plot(t_sine, shifted_sine[0])
plt.title('Shifted Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

#sawtooth normal
plt.figure(figsize=(8, 4))
plt.plot(t_sawtooth, sawtooth_wave)
plt.title('Original Sawtooth Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

#sawtooth scaled faster
plt.figure(figsize=(8, 4))
plt.plot(t_sawtooth_fast, sawtooth_fast)
plt.title('Fast Sawtooth Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

#sawtooth scaled slower
plt.figure(figsize=(8, 4))
plt.plot(t_sawtooth_slow, sawtooth_slow)
plt.title('Slow Sawtooth Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

#sawtooth shifted
plt.figure(figsize=(8, 4))
plt.plot(t_sawtooth, shifted_sawtooth[0])
plt.title('Shifted Sawtooth Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

# hello


























