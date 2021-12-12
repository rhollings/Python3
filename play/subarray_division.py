'''
Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

The length of the segment matches Ron's birth month, and,
The sum of the integers on the squares is equal to his birth day.
Determine how many ways she can divide the chocolate.

s = [2, 2, 1, 3, 2]
d = 4
m = 2

Lily wants to find segments summing to Ron's birth day, 4 
with a length equalling his birth month, 2. 
In this case, there are two segments meeting her criteria: [2, 2] and [1, 3].

Function Description

Complete the birthday function in the editor below.

birthday has the following parameter(s):

int s[n]: the numbers on each of the squares of chocolate
int d: Ron's birth day
int m: Ron's birth month
Returns

int: the number of ways the bar can be divided
'''


def birthday(s, d, m):
    count = 0
    
    for i in range(len(s)):
        try:
            if sum(s[i:i+m]) == d:
                count += 1
        except:
            pass
            
    return count
