'''
Given a non-empty array N, of non-negative integers , the degree of this array is defined as the maximum frequency of any one of its elements. Your task is to find the smallest possible length of a (contiguous) subarray of N, that has the same degree as N. For example, in the array [1 2 2 3 1], integer 2 occurs maximum of twice. Hence the degree is 2.

Input

Test case input contains 2 lines.
First line contains an integer T, representing the number of elements in the array.
The second line contains the array N, list of T integers each separated by space.

Output

Print the length of the smallest contiguous subarray of input array N, that has the same degree as N.
Code evaluation is based on your output, please follow the sample format and do NOT print anything else.
'''

import fileinput

inputData = ''

for line in fileinput.input():
    inputData += line


def codeHere():
    counter = 0
    num = 0
    for i in inputData:
        current = inputData.count(i)
        if current > counter:
            counter = current
            num = i
    return i


print(codeHere())
