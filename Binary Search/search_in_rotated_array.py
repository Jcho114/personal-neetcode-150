"""
33. Search in Rotated Sorted Array

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List

def search(nums: List[int], target: int) -> int:
  l, r = 0, len(nums)-1
  while l < r:
    c = (l+r) // 2
    if nums[c] > nums[r]:
      l = c + 1
    else:
      r = c
  offset = l
        
  l, r = 0, len(nums)-1
  while l <= r:
    c = (l+r) // 2
    offsetted = (c+offset) % len(nums)
    if nums[offsetted] < target:
      l = c + 1
    elif nums[offsetted] > target:
      r = c - 1
    else:
      return offsetted
        
  return -1

"""
We first find by how many values the list is rotated. We do this
by finding the position of the minimum index.
Once we do that, we can perform normal binary search, but this time
the left and right pointers are adpated to match the offset
caused by the initial rotation.

TC: O(lgn)
SC: O(1)
"""