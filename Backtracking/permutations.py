"""
46. Permutations

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]
"""

def permute(nums: list[int]) -> list[list[int]]:
  res = []
  def backTracking(perm: list[int], pool: list[int]) -> None:
    if not pool:
      res.append(perm)
    for num in pool:
      backTracking(perm+[num], list(filter(lambda el: el != num, pool)))
  backTracking([], nums.copy())
  return res

"""
There are n! possible ways to permute a list of size n.
Each permutation is of size n.
Let's portray the processing of permuting like this:
When permuting a list of size n, we pick one of the elements and add
it to our current list.
This leaves us with n-1 elements left.
If we keep repeating this process, we will eventually have 0 elements
left.
In this case, we append the current list to the result.
Let's call the remaining elements to choose from the "pool".
This is the argument we will have in addition to our current list,
which we can call "perm".
Implementation can be done in different ways, but I just used
list addition and a filter function.

Time Complexity: O(n!)?
Space Complexity: I need more time to think this one out lmao
"""