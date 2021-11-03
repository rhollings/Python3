'''
Alphabet Soup

Problem: Given a string of alphabetical characters following the rules as seen below, return a new string with the characters in alphabetical order.
Capital letters should appear before the same  lowercase letter(s) ex. (aBbbCcDdef). There will be no spaces in any strings.

Sample Input/Output:

A.) Input: "hello"  Output: "ehllo"
B.) Input: "eLEPhAnt" Output: "AEehLnPt"

'''

# attempt 1

def alphabet_soup(string):
  li = sorted(list(string)) # creates a list and sorts the letters
  new_string = ''
  for char in li: #iterate thru list and add to new_string
    new_string += char
    
  return new_string

word = input('Enter a String: ')
print(aplhabet_soup(word))

# attempt 2 

