import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


def signals():

    print("generating signals: ")
    sine_wave = generate_sine_wave(2, 1, 2, 100)
    sawtooth_wave = generate_sawtooth_wave(3, 0.4, 2, 100)

    print("applying time shifting: ")
    sine_shifted = time_shift_signal(sine_wave, 1, 100) 
    sawtooth_shifted = time_shift_signal(sawtooth_wave, 0.5, 100)  

    print("applying time scaling:")
    sine_fast = time_scale_signal(sine_wave, 2, 100)
    sine_slow = time_scale_signal(sine_wave, 0.5, 100)
    sawtooth_fast = time_scale_signal(sawtooth_wave, 2, 100)
    sawtooth_slow = time_scale_signal(sawtooth_wave, 0.5, 100)

    # Create time arrays for plotting
    t_original = np.linspace(0, 2, len(sine_wave))
    t_fast = np.linspace(0, 1, len(sine_fast))  
    t_slow = np.linspace(0, 4, len(sine_slow)) 


