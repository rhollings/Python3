# tips for working with strings 

return strParam[::-1] # returns a string reversed 

for str in string: #iterates thru a string
  print(str)
  if str == 'whatever':
    print('this')

    
'''
splt and join function:
given a string of space separated words, return a string with dash seperated words.

ex. this is a string
this-is-a-string
'''

def split_and_join(line):
  line = line.split(" ")
  line = "-".join(line)
  return line
# ====OR=====
def split_adn_join(line):
  line = line.replace(" ", "-")
  return line 
