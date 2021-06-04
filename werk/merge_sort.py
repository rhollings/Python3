def merge_sort(list):
  #sort in ascending order
  
  if len(list) <= 1: #stop condition for small list
    return list
  left_half, right_half = split(list)
  left = merge_sort(left_half) #recrusive !!!
  right = merge_sort(right_half)
  
  return merge(left, right)

def split(list):
  
  mid = len(list)//2
  left = list[:mid]
  right = list[mid:]
  
