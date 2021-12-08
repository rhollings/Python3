'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
Ex. arr = [1,2,3], [4,5,6], [7,8,9]]
'''

def diagonalDifference(arr):
    left1, left2, left3 = arr[0][0], arr[1][1], arr[2][2]
    right1, right2, right3 = arr[0][2], arr[1][1], arr[2][0]
    left = left1 + left2 + left3
    right = right1 + right2 + right3
    sum0 = left - right
    sum1 = right - left
    return abs(sum1)

  
  def diagonalDifference(arr):
    num = len(arr)
    first = 0
    second = 0
    for i in range(0, num):
        first += arr[i][i]
        second += arr[i][num - i - 1]
        
    return abs(first - second)
