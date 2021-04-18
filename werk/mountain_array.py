'''ex. arr = [0,3,2,1]  
        = true
       arr = [3,5,5]
        = false
'''

def validMountainArray(self, arr: List[int]) -> bool:
        
  if len(arr) < 3:
      return False
  left = 0
  for i in range(len(arr)-1):
      if arr[i+1] <= arr[i]:
          left = i
          break
  right = 0
  for i in range(len(arr)-1, 0, -1):
      if arr[i-1] <= arr[i]:
          right = i
          break
  if left == right and left > 0 and right+1 < len(arr):
      return True
  return False
