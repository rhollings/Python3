'''
A pangram is a sentence that contains every single letter of the alphabet at least once. 
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, 
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. 
Ignore numbers and punctuation.
'''
import string

pangram = "The quick, brown fox jumps over the lazy dog!"

def pangrams(s):
    # Write your code here
    s = s.lower()
    alphabets_lower = list(string.ascii_lowercase) 
    for alpha in alphabets_lower:
        if not alpha in s:
            return 'not pangram' 
    return 'pangram'

# make dict, if the dict has 26 chars, then all letters are there 
def pangrams(s):
    d={}
    for i in s.replace(' ',''):
        if i.lower() not in d:
            d[i.lower()]=1
        if len(d)==26:
            return 'pangram'
    return 'not pangram'
#

return 'pangram' if len(set(s.replace(' ','').lower()))==26 else 'not pangram'
