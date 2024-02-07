"""
215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""

import heapq

def kth_largest_element(nums: list[int], k: int) -> int:
  nums = [-num for num in nums]
  heapq.heapify(nums)
  for _ in range(1,k):
    heapq.heappop(nums)
  return -nums[0]

"""
Self-explanatory.
Idk why this is a leetcode medium tbh.

Time Complexity: O(nlgn)
Space Complexity: O(1)
"""