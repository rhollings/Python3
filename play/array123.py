# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True


def array123(nums):
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3: #checks if all are true
      return True
  return False
# =======================================================
# Sorting function
# example of how to sort through a list, str, array for nth smallest/largest element

SelectionSort(List) {
  for(i from 0 to List.Length) {
    SmallestElement = List[i] #LargestElement = List[i] <= Opposite
    for(j from i to List.Length) {
      if(SmallestElement > List[j]) {
        SmallestElement = List[j]
      }
    }
    Swap(List[i], SmallestElement)
  }
}
