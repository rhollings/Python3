'''
Sherlock considers a string to be valid if all characters of the string appear the same number of times.
It is also valid if he can remove just 1 character at 1 index in the string, and the remaining characters will occur the same number of times.
Given a string , determine if it is valid. If so, return YES, otherwise return NO.

Example: 
s = abc 
This is a valid string because frequencies are {a:1, b:1, c:1} 

s = abcc
This is a valid string because we can remove one c and have 1 of each character in the remaining string.

s= abccc
This string is not valid as we can only remove 1 occurrence of c. That leaves character frequencies of {a:1, b:1, c:2}.


'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    freq = {c:0 for c in s}
    
    for c in s:
        freq[c]+=1
    
    freq = list(freq.values())
    freq.sort()
    uniques = [freq[0]]
    
    n = len(freq)
    for i in range(1,n):
        if freq[i]!=freq[i-1]:
            uniques.append(freq[i])
    
    if len(uniques)>2:
        return 'NO'
      
    if len(uniques)!=1:
        w = sum(freq)
        mx = max(freq)
        mn = min(freq)
        if (mn*n)+1!=w and (mx*(n-1))+1!=w:
            return 'NO'
    return 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
