"""
From Codewars by Rubikan

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""

#My Solution

def rot13(message):
    res = ''
    for item in message:
        if  (item >= 'A' and item <= 'M') or (item >= 'a' and item <= 'm'):
            res += chr(ord(item)+13)
        elif  (item >= 'N' and item <= 'Z') or (item >= 'n' and item <= 'z'):
            res += chr(ord(item)-13)
        else:
            res += item
    return res
  
"""
  ROT13 ("Rotate by 13 places", sometimes a hyphen of ROT-13) is a simple letter substitution password, replacing the letter with the 13th letter of the alphabet. ROT13 is a special case of the Caesar cipher invented in ancient Rome.

Because there are 26 letters in the basic Latin alphabet, ROT13 is its own inverse; that is, to undo ROT13, the same algorithm works, so the same operation can be used for encoding and decoding. The algorithm provides little security for encryption and is often cited as a typical example of weak encryption [1].

ROT13 is used in online forums as a means of hiding spoilers, whispers, riddles and offensive material. ROT13 is described as "a US version of the magazine, and its answer is reversed." [2] ROT13 has triggered a variety of letters and word games on the Internet, and is often mentioned in newsgroup conversations.

ROT13 encryption/decryption process.
Encryption and decryption uses a process: replace ABCDEFGHIJKLM with NOPQRSTUVWXYZ in turn, and replace NOPQRSTUVWXYZ with ABCDEFGHIJKLM.
"""
