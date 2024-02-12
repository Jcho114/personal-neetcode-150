"""
200. Number of Islands
Given an m x n 2D binary grid grid which represents a map of '1's (land) and
'0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are
all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

def num_of_islands(grid: list[list[int]]) -> int:
  def dfs(r: int, c: int) -> None:
    if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r]) and grid[r][c] == "1":
      grid[r][c] = "0"
      dfs(r-1,c)
      dfs(r+1,c)
      dfs(r,c-1)
      dfs(r,c+1)
  res = 0
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      if grid[r][c] == "1":
        dfs(r, c)
        res += 1
  return res

"""
Remember that an island is basically a sequence of "1"s where for each "1" there
is another "1" either above, below, left, or right of it.
How do we find an array?
If we iterate through all the elements we can determine if we found an island
if we hit a "1".
But how do we not overcount? Let's remove it!
To do that we use dfs (standard).
Eventually we have an empty grid and the total number of islands.

Time Complexity: O(n^2)
Space Complexity: O(1) if you don't consider stack frame, otherwise O(n^2)?
"""