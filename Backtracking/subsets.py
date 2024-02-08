"""
78. Subsets

Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
"""

def subsets(nums: list[int]) -> list[list[int]]:
  res = []
  def backTracking(i, lst):
    if i >= len(nums):
      res.append(lst)
    else:
      backTracking(i+1, lst)
      lst = lst + [nums[i]]
      backTracking(i + 1, lst)
  backTracking(0, [])
  return res

"""
Can convert problem to a decision tree.
At index 0, we have two decisions:
1. Do we include the element at this index?
2. Do we don't?
We can basically do the first choice, then backtrack, then do the second choice.
After each choice, we get another pair of choices but for the next element.
We keep doing this until we reach the end of the list.

Time Complexity: O(2^n)
Space Complexity: Not exactly sure, gonna have to think about it again later
"""