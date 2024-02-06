"""
746. Min Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
"""

"""
dp[0] = dp[1] = 0
dp[2] = min(dp[2-1] + cost[2-1], dp[2-2] + cost[2-2])
dp[3] = min(dp[3-1] + cost[3-1], dp[3-2] + cost[3-2])
"""

def min_cost_climbing_stairs(cost: list[int]) -> int:
  dp = [0 for i in range(len(cost) + 1)]
  for i in range(2, len(cost)+1):
    dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
  return dp[-1]

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""