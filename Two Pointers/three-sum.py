"""
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

def three_sum(nums):
  nums = sorted(nums)
  res = []
  combs = set()
  for m in range(1, len(nums)-1):
      l, r = 0, len(nums)-1
      while l < m and m < r:
          sum = nums[l] + nums[m] + nums[r]
          if sum == 0:
              if (nums[l],nums[m],nums[r]) not in combs:
                  res.append([nums[l], nums[m], nums[r]])
                  combs.add((nums[l],nums[m],nums[r]))
              l += 1
              r -= 1
              while l < m and nums[l] == nums[l - 1]:
                  l += 1
          elif sum < 0:
              l += 1
          else:
              r -= 1
  return res

"""
Note that I have yet to clean the code up

Time Complexity: O(n^2)
Space Complexity: O(n)
"""