import numpy as np
from signals import * 

def test_generate_sine_wave():
    """
    Test the generate_sine_wave function with various test cases
    """

    y = generate_sine_wave(2, 1, 2, 100) #this test is for signal length
    assert len(t) == 1000

    y = generate_sine_wave(0, 1, 2, 100) #this test is for frequency 0
    assert np.isclose(y, 0).all() 

    y = generate_sine_wave(1, 2, 1, 1000)
    assert np.isclose(y[0], 0, atol=1e-6)  #this test is for checking first value at t=0        

    y = generate_sine_wave(5, 3, 1, 1000)
    assert np.isclose(max(y), 3, atol=1e-6)  #this test is for checking max amplitude

    print("\N{grinning face}")

def test_generate_sawtooth_wave():
    """
    Test the generate_sawtooth_wave function with various test cases
    """

    y = generate_sawtooth_wave(3, 0.4, 2, 100) #this test is for signal length
    assert len(y) == 200

    y = generate_sawtooth_wave(0, 1, 2, 100) #this test is for frequency 0
    assert np.isclose(y, 0).all() 

    y = generate_sawtooth_wave(1, 2, 1, 1000)
    assert np.isclose(y[0], -2, atol=1e-6)  #this test is for checking first value at t=0        

    y = generate_sawtooth_wave(5, 3, 1, 1000)
    assert np.isclose(max(y), 3, atol=1e-6)  #this test is for checking max amplitude   

     

    


