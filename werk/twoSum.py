'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

######################################################

#   Brute Force Approach

#   Runtime: 4052ms   -   23.64%
#   Memory: 14.7MB  -   92.77%

######################################################


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target: return [i, j]


######################################################

#   Approach - 2: Sorting the array

#   Runtime: 60ms   -   71.32%
#   Memory: 14.7MB  -   91.13%

######################################################

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Sorting the array and storing in a var
        sortedNums = sorted(nums)
        
        # Declaring pointers to start and end of array
        i = 0
        j = len(nums) - 1
        
        while i < j:

            # Case 1: target found
            if sortedNums[i] + sortedNums[j] == target:

                # To find Indices of the sortedNums[i], sortedNums[j] in actual array
                ith = 0
                jth = 0
                
                # Looping through nums array to find indcies
                for k in range(len(nums)):
                    if nums[k] == sortedNums[i]:
                        ith = k
                        break
                
                for k in range(len(nums)):
                    # Why we add k != ith is there may be a case like target = 6 and
                    # there are 2 3's in array.
                    # To skip first index of 3, since it is noted already by above 
                    # loop for ith index
                    if nums[k] == sortedNums[j] and k != ith:
                        jth = k
                        break
                
                return [ith, jth]

            # Case 2: sum > target
            if sortedNums[i] + sortedNums[j] > target:
                # It happens since array is sorted and jth index value is bigger than
                # needed. so decrement jth pointer by 1
                j -= 1

            # Case 3: sum < target
            else:
                # It happens since array is sorted and ith index value is smalled than
                # needed. so increment ith pointer by 1 
                i += 1

######################################################

#   Approach - 3: Using a Dictionary

#   Runtime: 56ms   -   83.65%
#   Memory: 15.2MB  -   50.37%

######################################################

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Using dictionary to store key-value pairs of nums[i], i
        dictionary = dict()
        
        for i in range(len(nums)):
            
            # Checking if target - nums[i] is already present in dict.
            # If yes, we have found the pair and we return
            # dictionary[target - nums[i]] which has value as index of that element
            # and i, which is index of nums[i]
            if target - nums[i] in dictionary:
                return [dictionary[target - nums[i]], i]
            
            # Else, we add nums[i], i as key-value pair to dict
            dictionary[nums[i]] = i

            
######################################################

#   Approach - 4: Binary Search

#   Runtime: 137ms   -   83.23%
#   Memory: 14.9MB  -   91.21%

######################################################  

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            left = 0
            right = len(numbers)-1

            while left<right:
                sum_ = numbers[left]+numbers[right] 
                if sum_ < target:
                    left +=1
                elif sum_ > target:
                    right -=1
                else:
                    return[left+1,right+1]
