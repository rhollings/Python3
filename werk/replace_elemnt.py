'''
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
'''

def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        #if array has only one element, we return [-1]
        if len(arr) == 1:
            return [-1]
        
        #for more elements we loop at ech of them,
        #and the last we assign the last element as -1
        
        else:
            for index in range(0, len(arr)-1, 1):
                arr[index] = max(arr[index + 1:])
                
            arr[len(arr) - 1] = -1
        return arr
