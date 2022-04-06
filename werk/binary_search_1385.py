'''
Given two integer arrays arr1 and arr2, and the integer d, 
return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] 
such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
'''

# First Approach (not binary) 152ms O(n^2)
def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0 
        for i in arr1:
            count = 1
            for j in arr2:
                if abs(i - j) <= d:
                    count = 0
                    break
            ans += count
        return ans


# Binary Approach   90ms O(logn)
def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        result = len(arr1)
        arr2.sort()
        for num in arr1:
            index = bisect.bisect(arr2, num)
            if index < len(arr2) and abs(num - arr2[index]) <= d:
                result -= 1
                continue
            if index > 0 and abs(num - arr2[index - 1]) <= d:
                result -= 1
                continue
        return result

'''
Example 1:

Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation: 
For arr1[0]=4 we have: 
|4-10|=6 > d=2 
|4-9|=5 > d=2 
|4-1|=3 > d=2 
|4-8|=4 > d=2 
For arr1[1]=5 we have: 
|5-10|=5 > d=2 
|5-9|=4 > d=2 
|5-1|=4 > d=2 
|5-8|=3 > d=2
For arr1[2]=8 we have:
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2
'''
