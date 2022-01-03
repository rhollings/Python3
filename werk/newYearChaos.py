#!/bin/python3

import math
import os
import random
import re
import sys

#
'''
It is New Year's Day and people are in line for the Wonderland rollercoaster ride.
Each person wears a sticker indicating their initial position in the queue from 1 to n.
Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker.
One person can bribe at most two others.

Determine the minimum number of bribes that took place to get to a given queue order.
Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.
'''

# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here

    c = 0
    total = 0

    for i in range(len(q),0,-1): 
        for j in range(len(q)-1,-1,-1):
            if q[j] != i:
                c += 1
                if c > 2:
                    print("Too chaotic")
                    return
            else:
                total += c
                c = 0
                q.pop(j)
                break
    print(total)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
