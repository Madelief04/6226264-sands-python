Signal Processing Project
This project generates sine and sawtooth waves and performs time shifting and scaling operations.

files:
- signals.py - generated a sine and a sawtooth signal with 2 operations : time shifting and time scaling
- run.py - script that generates and plots the signals
- actualprojectfile.py - first version of signals.py
- hello.py - to test my first file in my repository
- oefenenmetcommands.py - to practise the commands through the terminal
- test_my_function.py - comprehensive test suite for all functions

project structure: 
signals.py contains four functions
- generate_sine_wave() - creates a sine wave signal
- generate_sawtooth_wave() - creates a sawtooth wave signal (width=0 for rising, width=1 for falling)
- time_shift_signal() - time shifts the initial signals
- time_scale_signal() - time scales the initial signals

The parameters that I used for both signals are: frequency, amplitude, duration, sampling_rate (plus width for sawtooth)

run.py generates and plots 8 individual plots:
- 4 plots for my sine wave signal: normal, slowed ×0.5, fasted ×2 and shifted
- 4 plots for ,y sawtooth wave signal: normal, slowed ×0.5, fasted ×2 and shifted

Documentation:
All my functions include detailed docstrings explaining parameters, return values, and usage.

Tests:
My project also includes tests that verify sine wave generation, sawtooth wave generation, time shifting functionality, time scaling operations, and edge cases.

How to run:
python run.py
python test_my_function.py
