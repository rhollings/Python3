'''
Write a function with the signature shown below:

def is_int_array(arr):
    return True
returns true / True if every element in an array is an integer or a float with no decimals.
returns true / True if array is empty.
returns false / False for every other input.
'''

def is_int_array(arr):
    if arr == []:
        return True
    if arr in [None, ""]:
        return False
    for i in arr:
        if type(i) in [int, float]:
            if int(i) != i:
                return False
        else:
            return False
    return True
