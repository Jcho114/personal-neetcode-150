"""
417. Pacific Atlantic Water Flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
"""

from typing import List
from collections import deque

def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
  directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
  pacificVisited = set()
  queue = deque()

  def isInRange(i, j):
      return i >= 0 and i < len(heights) and j >= 0 and j < len(heights[i])

  for i in range(len(heights)):
    if i == 0:
      for j in range(len(heights[i])):
        queue.append([0, j])
    else:
      queue.append([i, 0])
        
  while queue:
    i, j = queue.popleft()
    if (i, j) not in pacificVisited:
      pacificVisited.add((i, j))
      for di, dj in directions:
        ni, nj = i+di, j+dj
        if isInRange(ni, nj) and heights[ni][nj] >= heights[i][j]:
          queue.append([ni, nj])
        
  for i in range(len(heights)):
    if i == len(heights)-1:
      for j in range(len(heights[i])):
        queue.append([len(heights)-1, j])
    else:
      queue.append([i, len(heights[i])-1])
        
  atlanticVisited = set()
  res = []
  while queue:
    i, j = queue.popleft()
    if (i, j) not in atlanticVisited:
      atlanticVisited.add((i, j))
      for di, dj in directions:
        ni, nj = i+di, j+dj
        if isInRange(ni, nj) and heights[ni][nj] >= heights[i][j]:
          queue.append([ni, nj])
        if (i,j) in pacificVisited:
          res.append([i,j])
        
  return res

"""
Perform BFS to simulate both the pacific and atlantic rainflow, respectively.
Then find the intersection of the rainflows and return it.

TC: O(n*m)
SC: O(n*m)
"""