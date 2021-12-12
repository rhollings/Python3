'''
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with  places after the decimal.

Example
arr = [1, 1, 0, -1, -1]
There are  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:
0.400000
0.400000
0.200000
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
# My Code Below
def plusMinus(arr):
    arr = sorted(arr)
    pos, neg, zero = 0, 0, 0
    size = len(arr)
    for i in arr:
        if i < 0:
            neg += 1
        elif i == 0:
            zero += 1
        else:
            pos += 1
    pos = pos / size
    neg = neg / size
    zero = zero /size
    
    print('%.6f' % pos + "\n" + '%.6f' % neg + "\n" + '%.6f' % zero)

# TESTS  
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
