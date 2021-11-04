def binary_search(list, target):
  first = 0
  last = len(list) - 1
  
  while first <= last:
    midpoint = (first + last)//2
    
    if list[midpoint] == target:
      return midpoint
    elif list[midpoint] < target:
      first = midpoint + 1
    else:
      last = midpoint - 1
  
  return None 

#invert binary tree

'''
def inver_tree(tree):
  if tree is None:
    return tree.left, tree.right = tree.right, tree.left
  invert_tree(left.tree)
  invert_tree(right_tree)
'''
