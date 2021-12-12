'''
There is a large pile of socks that must be paired by color. 
Given an array of integers representing the color of each sock,
determine how many pairs of socks with matching colors there are.

'''

def sockMerchant(n, ar):
    colorCount = [0] * 100 #because the ar maxes at 100
    pairs = 0
    for sock in ar:
        colorCount[sock - 1] += 1 #@ index of sock - 1 // colorCount[3-1] += 1 OR colorCount[3-1] = [3-1] + 1 
        if (colorCount[sock - 1] % 2 == 0):
            pairs += 1
    return pairs
