'''
Given two seperate lists of strings, return a list combining the two strings.

Ex. str1 = ['name1', 'name2', 'name3', 'name4', 'name5']
    str2 = ['apples', 'oranges', 'pears', 'strawberries', 'watermelon']
return 
  name1:  apples
  name2:  oranges
  name3:  pears
  name4:  strawberries
  name5:  watermelon
  
'''

def who_what(a, b):
    sentence = ''
    i = 0 
    while i <= len(a) - 1:
        name = a[i]
        i += 1
        j = 0 
        while j <= len(b) - 1: #dub while loop to specify elem. // won't work if list size is unmatched
            fruit = b[j]
            if b.index(fruit) == a.index(name): #needed index() to grab elems at same place
                print(name + ' likes ' + fruit)
            j += 1
 
# Runs O(2n^2) ??
