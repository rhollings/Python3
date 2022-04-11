
#O(n)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if nums[i] == target:
                start = i
                while i+1 < len(nums) and nums[i+1] == target:
                    i += 1
                return [start, i]
        return [-1, -1]
      

#O(logn)
class Solution:
    def findStart():
        pass
    def findEnd():
        pass
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = findStart()
        end = findEnd()
        return [start, end]
