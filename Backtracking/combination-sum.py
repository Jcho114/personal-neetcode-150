"""
39. Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of
candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency
of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations
for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []
"""

def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
  res = []
  def backTracking(i: int, subset: list[int], total: int) -> None:
    if i >= len(candidates):
      if total == target:
        res.append(subset)
    elif total <= target:
      # We choose to not include nums[i]
      backTracking(i+1, subset, total)
      subset = subset + [candidates[i]]
      # We choose to include nums[i] "one more time"
      backTracking(i, subset, total+candidates[i])
  backTracking(0, [], 0)
  return res

"""
Similar to the backtracking question.
First we have a decision tree where for each node we have to choose between:
1. We do not include the current element
2. We do include it "one more time" (since we can include it multiple times)
Due to the nature of the second decision, we have to also add a clause where
if the sum of the subset is greater than the target, executition of that decision
end.

Time Complexity: O(2^n)
Space Complexity: Have to think about it more
"""