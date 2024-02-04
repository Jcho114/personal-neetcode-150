"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

def two_sum(nums: list[int], target: int) -> list[int]:
  sum = {}
  for i in range(len(nums)):
      num = nums[i]
      # Check if necessary number is already in the dictionary
      if target-num in sum:
          # If it is in the dict return the index pair
          return [sum[target-num], i]
      # Keep track of index of current number for future reference
      sum[num] = i
  # Returned pair if there is no sum
  return [-1, -1]

"""
Use a dictionary to store elements and their indices as key value pairs.
As we iterate through the nums list, if there is a number stored in the
dictionary that, along with the current element, sums to target, return
the corresponding index pair.

Time Complexity: O(n)
Space Complexity: O(n)
"""