
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
    def find_start(nums, target):
        if nums[0] == target:
            return 0
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target and arr[mid-1] < target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def find_end():
        if nums[-1] == target:
            return len(arr) - 1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target and arr[mid+1] < target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or nums[0] > target or nums[-1] < target:
            return [-1, -1]
        start = find_start(nums, target)
        end = find_end(nums, target)
        return [start, end]
