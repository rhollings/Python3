'''
Bomberman lives in a rectangular grid. Each cell in the grid either contains a bomb or nothing at all.

Each bomb can be planted in any cell of the grid but once planted, it will detonate after exactly 3 seconds. 
Once a bomb detonates, it's destroyed — along with anything in its four neighboring cells. 
This means that if a bomb detonates in cell i,j any valid cells (i+1,j) and (i,j+1) are cleared. 
If there is a bomb in a neighboring cell, the neighboring bomb is destroyed without detonating, so there's no chain reaction.

Bomberman is immune to bombs, so he can move freely throughout the grid. Here's what he does:

Initially, Bomberman arbitrarily plants bombs in some of the cells, the initial state.
After one second, Bomberman does nothing.
After one more second, Bomberman plants bombs in all cells without bombs, thus filling the whole grid with bombs. No bombs detonate at this point.
After one more second, any bombs planted exactly three seconds ago will detonate. Here, Bomberman stands back and observes.
Bomberman then repeats steps 3 and 4 indefinitely.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    
    # main optimization is realising that for n >= 3:
    # the odd iterations of n just alternate between 2 arrays, n = 3 and n = 5
    
    def explode(arr): # simulate an explosion 
        newGrid = []
        for i in range(len(arr)):
            row = ''
            for j in range(len(arr[0])):
                center = arr[i][j] == 'O'
                up = i > 0 and arr[i-1][j] == 'O'
                down =  i < (len(arr) - 1) and arr[i+1][j] == 'O'
                left = j > 0 and arr[i][j-1] == 'O'
                right = j < len(arr[0]) - 1 and arr[i][j+1] == 'O'
                
                row += '.' if center or up or down or left or right else 'O'
            newGrid.append(row)
            
        return newGrid
        
    if n == 1: # return original array if n = 1
        return grid
    elif n % 2 == 0: # return full array if even (bomberman places down all charges)
        return [''.join(['O' for _ in range(len(grid[0]))]) for _ in range(len(grid))]
    else:
        if int(n/2) % 2 == 1: # n = 3, 7, 11...
            return explode(grid)
        else: # n = 5, 9, 13
            return explode(explode(grid))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
