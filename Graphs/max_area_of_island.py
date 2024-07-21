"""
695. Max Area of Island

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""

from typing import List

def maxAreaOfIsland(grid: List[List[int]]) -> int:
  res = 0
  directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  
  def dfs(i, j):
    if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[i]) and grid[i][j] == 1:
      grid[i][j] = 0
      return 1 + sum(dfs(i+dx, j+dy) for dx, dy in directions)
    return 0
  
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == 1:
        res = max(res, dfs(i, j))
  
  return res

"""
Similar to number of islands problem where we use dfs. This time, however, we
keep track of the size of each island and keep a variable to keep track of the
largest island.

TC: O(n^2)
SC: O(n^2) WC if there is one huge island
"""