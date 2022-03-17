'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
'''

# MY ATTEMPT

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        length = len(strs[0]) #length of first word
        count = len(strs)
        for i in range(length):
            c = strs[0][i]
            for j in range(1, count):
                if len(strs[j]) == i or strs[j][i] != c:
                    return strs[0][:i]
        return strs[0]

# FASTEST TIME 

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minn = min([len(x) for x in strs])
        if minn == 0:
            return ""
                   
        string = ""
        c = strs[0][0]
        i = 0
        
        
        while i < minn:
            for word in strs:
                if word[i] != c:
                    return string
            string += c
            i += 1
            if i < minn:
                c = strs[0][i]
            
        return string
