'''
You will be given a list of 32 bit unsigned integers. Flip all the bits (0 => 1 and 1 => 0 ) and return the result as an unsigned integer.
'''



def flippingBits(n):
    return (2**32 - 1) - n
