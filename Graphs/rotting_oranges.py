"""
994. Rotting Oranges

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""

from typing import List
from collections import deque

def orangesRotting(grid: List[List[int]]) -> int:
  queue = deque()
  directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
  
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == 2:
        queue.append((i, j, 0))
  
  m = 0
  while queue:
    i, j, m = queue.popleft()
    for dx, dy in directions:
      nx, ny = i+dx, j+dy
      if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[nx]) and grid[nx][ny] == 1:
        grid[nx][ny] = 2
        queue.append((i+dx, j+dy, m+1))
  
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == 1:
        return -1
  
  return m

"""
Find all of the rotten oranges first. Add them to a queue.
Afterwards, perform dfs on these oranges at the same time.
Once we finish our dfs, we either have made all the oranges
rotten or we still have fresh ones left.
If the former, we return how many bfs steps it took.
If the latter, we return -1.

TC: O(n)
SC: O(n)
"""