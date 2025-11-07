import numpy as np
from signals import * 

# Your test function
def test_generate_sine_wave():
    """
    Test the generate_sine_wave function with various test cases
    """

    y, t = generate_sine_wave(2, 1, 2, 100) #this test is for signal length
    assert len(t) == 200

    y, t= generate_sine_wave(0, 1, 2, 100) #this test is for frequency 0
    assert np.isclose(y, 0).all() 

    y, t = generate_sine_wave(1, 2, 1, 1000)
    assert np.isclose(y[0], 0, atol=1e-6)  #this test is for checking first value at t=0        

    y, t = generate_sine_wave(5, 3, 1, 1000)
    assert np.isclose(max(y), 3, atol=1e-6)  #this test is for checking max amplitude

    print("it passed all tests \U0001F601!!!")


def test_generate_sawtooth_wave():
    """
    Test the generate_sawtooth_wave function with various test cases
    """

    y, t = generate_sawtooth_wave(3, 0.4, 2, 100) #this test is for signal length
    assert len(t) == 200

    y, t= generate_sawtooth_wave(0, 0.4, 2, 100) #this test is for frequency 0
    assert np.isclose(y, 0).all() 

    y, t = generate_sawtooth_wave(1, 1, 1, 1000)
    assert np.isclose(y[0], -1, atol=1e-6)  #this test is for checking first value at t=0        

    y, t = generate_sawtooth_wave(5, 2, 1, 1000)
    assert np.isclose(max(y), 2, atol=1e-6)  #this test is for checking max amplitude

    print("it passed all tests \U0001F601!!") 



    



     

    


