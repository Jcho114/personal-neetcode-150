"""
130. Surrounded Regions

You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.
"""

from typing import List
from collections import deque

def solve(board: List[List[str]]) -> None:
  directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
  prohibited = set()
  queue = deque()
  
  for i in [0, len(board)-1]:
    for j in range(len(board[i])):
      if board[i][j] == "O":
        queue.append((i, j))
  
  for i in range(len(board)):
    for j in [0, len(board[i])-1]:
      if board[i][j] == "O":
        queue.append((i, j))
  
  while queue:
    i, j = queue.popleft()
    prohibited.add((i, j))
    for di, dj in directions:
      ni, nj = i+di, j+dj
      if ni >= 0 and ni < len(board) and nj >= 0 and nj < len(board[ni]) and board[ni][nj] == "O" and (ni, nj) not in prohibited:
        queue.append((ni, nj))

  def dfs(i, j):
    if i > 0 and j > 0 and i < len(board)-1 and j < len(board[i])-1 and board[i][j] == "O":
      board[i][j] = "X"
      for dx, dy in directions:
        dfs(i+dx, j+dy)

  for i in range(1, len(board)-1):
    for j in range(1, len(board[i])-1):
      if board[i][j] == "O" and (i, j) not in prohibited:
        dfs(i, j)

"""
First perform bfs on all "O" values in the edge of the grid at the same time
to create a "prohibited" set of "O" values that should not be changed to "X".
Afterwards, perform dfs on all non-prohibited "O" values, changing them to
"X" as we traverse.

TC: O(n*m)
SC: O(n*m)
"""