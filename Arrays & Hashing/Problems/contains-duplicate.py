"""
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

def contains_duplicate(nums):
  s = set()
  for n in nums:
    if n in s:
      return True
    s.add(nums)
  return False

"""
Iterate through the nums list and add each number to a set.
If a number is already in the set, return True
If we iterate through the entire list, return False

Time Complexity: O(n) since we are iterating through the nums list
Space Complexity: O(n) since the set can contain all the elements if all the elements are unique
"""