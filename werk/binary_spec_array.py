'''
Runtime: 49 ms // faster than 60.59% 
Memory Usage: 14 MB less than 16.76% memory
'''

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for x in range(1, len(nums)+1):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < x:
                    left  = mid + 1
                else:
                    right = mid - 1
            if len(nums[left:]) == x:
                return x
        return -1
