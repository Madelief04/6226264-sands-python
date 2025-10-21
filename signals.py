import numpy as np

# sine wave with parameters frequency, amplitude, duration, sampling_rate
def generate_sine_wave (frequency, amplitude, duration, sampling_rate): 
    t = np.linspace(0, duration, int(sampling_rate * duration))
    signal = amplitude * np.sin(2 * np.pi * frequency * t)
    return signal

sine_wave = generate_sine_wave (2, 1, 2, 100)


""""generate a sine wave signal using the parameters frequency, amplitude, duration, and sampling_rate.
The function returns a numpy array representing the sine wave signal. """

# sawtooth wave with parameters frequency, amplitude, duration, sampling_rate, width =1
def generate_sawtooth_wave (frequency, amplitude, duration, sampling_rate, width =1 ): 
    t = np.linspace(0, duration, int(sampling_rate * duration))
    sawtooth_wave = amplitude * signal.sawtooth(2 * np.pi * frequency * t, width)
    return sawtooth_wave

sawtooth_wave = generate_sawtooth_wave (3, 0.4, 2, 100)

""""generate a sawtooth wave signal using the parameters frequency, amplitude, duration, sampling_rate, and width. 
The function returns a numpy array representing the sawtooth wave signal. """


#function for time shift
def time_shift_signal(signal, shift_seconds, sampling_rate):
    shift_samples = int(shift_seconds * sampling_rate)
    return (signal, shift_samples)

sine_shifted = time_shift_signal(sine_wave, 1, 5) 
sawtooth_shifted = time_shift_signal(sawtooth_wave, 2, 100)  

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

"""time scale a signal by a specified factor. The function takes a signal (numpy array), scale factor, and sampling rate as inputs.
It returns the time-scaled signal as a numpy array. """

sine_fast = time_scale_signal(sine_wave, 2, 100)
sine_slow = time_scale_signal(sine_wave, 0.5, 100)

sawtooth_fast = time_scale_signal(sawtooth_wave, 2, 100)
sawtooth_slow = time_scale_signal(sawtooth_wave, 0.5, 100)

""""time scale a signal by a specified factor. The function takes a signal (numpy array), scale factor, and sampling rate as inputs.""
""""It returns the time-scaled signal as a numpy array. """ 
