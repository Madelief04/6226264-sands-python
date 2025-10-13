files:
signals.py - generated a sine and a sawtooth signal with 2 operations : time shifting and time scaling
run.py - script that generates and plots the signals
actualprojectfile.py - first version of signals.py
hello.py - to test my first file in my repository
oefenenmetcommands.py - to practise the commands through the terminal

signals.py (used to be actualprojectfile.py)
i added a sin signal to my actualprojectfile.py to start and look if it works. it does. i can see it in my reposetory now. 
i changed the code into an actual sinusoidal signal in my actualprjectfile.py.

A define function is used for the sine wave.
A sawtooth function is added, using the same parameters plus the width. 
        width=0 gives a rising sawtooth, width=1 is a falling sawtooth signal. 
For both signals the parameters frequency, amplitude, duration and sampling_rate (and width for sawtooth) can be changed. 

The signal.py contains four functions. Generate_sine_wave for making a sine signal. Generege_sawtooth_wave for a sawtooth function. A time_shift_signal for time shifting the initial signals and a time_scale_signal for timescaling the inital fignals. 

The run.py file contains those function plus a plot for each function individually. For both the sine and sawtooth signal, a seperate plot is made for the signal that is slowed ( *0.5) and fasted (*2). (This values can be adjusted). And there is a plot for the shifted signals. This means in total 8 plots (4 for each signal; 1 normal signal and 3 with the operations). 
