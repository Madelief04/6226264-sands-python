import numpy as np
from signals import * 

def test_generate_sine_wave():
    """ Test the generate_sine_wave function with various test cases
    """
    y, t = generate_sine_wave(2, 1, 2, 100)
    assert len(t) == 200

    y, t= generate_sine_wave(0, 1, 2, 100)
    assert np.isclose(y, 0).all() 

    y, t = generate_sine_wave(1, 2, 1, 1000)
    assert np.isclose(y[0], 0, atol=1e-6)      

    y, t = generate_sine_wave(5, 3, 1, 1000)
    assert np.isclose(max(y), 3, atol=1e-6)

    print("it passed all tests \U0001F601!!!")


def test_generate_sawtooth_wave():
    """
    Test the generate_sawtooth_wave function with various test cases
    """

    y, t = generate_sawtooth_wave(3, 0.4, 2, 100) 
    assert len(t) == 200

    y, t= generate_sawtooth_wave(0, 0.4, 2, 100)
    assert np.isclose(y, 0).all() 

    y, t = generate_sawtooth_wave(1, 1, 1, 1000)
    assert np.isclose(y[0], -1, atol=1e-6)     

    y, t = generate_sawtooth_wave(5, 2, 1, 1000)
    assert np.isclose(max(y), 2, atol=1e-6) 

    print("it passed all tests \U0001F601!!") 

def test_time_shift_signal():
    """
    Test the time_shift_signal function with various test cases
    """

    signal = np.array([1, 2, 3, 4, 5])
    shifted_signal, shift_samples = time_shift_signal(signal, 2, 1)
    assert shift_samples == 2

    shifted_signal, shift_samples = time_shift_signal(signal, 0, 1) 
    assert shift_samples == 0

    print("it passed all tests \U0001F601!!!")  


def test_time_scale_signal():
    """
    Test the time_scale_signal function with various test cases
    """
    signal = np.array([1, 2, 3, 4, 5])
    scaled_signal = time_scale_signal(signal, 2, 1) 
    assert len(scaled_signal) == 2

    scaled_signal = time_scale_signal(signal, 0.5, 1)
    assert len(scaled_signal) == 10

    print("it passed all tests \U0001F601!!!")    






     

    


