"""
153. Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""

from typing import List

def findMin(nums: List[int]) -> int:
  l, r = 0, len(nums)-1
  while l < r:
    c = (l+r)//2
    if nums[c] > nums[r]:
      l = c+1
    else:
      r = c
  return nums[l]

"""
We know that at some "window" in the list all values will be sorted
in increasing order. We just have to find that window, then find the
start of it, which is the minimum value.
To do this, we perform binary search, where we have a left and right
pointer. We find the center pointer, and if the value in the center
if greater than the value in the right, we know that the aforementioned
window will be in the right. Otherwise, we know that the aforementioned
window should be to our left including the current value.
We follow this logic in code.

TC: O(lgn)
SC: O(1)
"""