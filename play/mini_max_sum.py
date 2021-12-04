'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Ex. arr = [1, 3, 5, 7, 9]
The minimum sum is 1 + 3 + 5 + 7 = 16 and the maximum sum is 3 + 5 + 7 + 9 = 24. The function prints 16 24
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr = sorted(arr)
    min = arr[:-1]
    max = arr[1:]
    x, y = 0, 0
    for i in min:
        x += i
    for i in max:
        y += i
    print(x, y)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
