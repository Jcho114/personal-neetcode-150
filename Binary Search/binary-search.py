"""
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""

def binary_search(nums, target):
  l, r = 0, len(nums)-1
  while l <= r:
    m = (l + r) // 2
    num = nums[m]
    if num < target:
      l = m+1
    elif num > target:
      r = m-1
    else:
      return m
  return -1

"""
Your standard binary search.
Personally went over this many times in class so I won't go into
too much detail.
In general you use a decrease and conquer algorithm where you have
two pointers 'l' and 'r' that you then use to get a center 'm'.
You compare the element in index 'm' and basically divide the
'searchable' part of the list in half depending on the result of
the comparison.
Side note, this only works on sorted lists.

Time Complexity: O(lgn)
Space Complexity: O(1)
"""