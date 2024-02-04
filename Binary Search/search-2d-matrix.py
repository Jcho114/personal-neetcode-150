"""
74. Search a 2D Matrix

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""

def binary_search_2d_matrix(matrix: list[list[int]], target: int) -> bool:
  # Isolate to a single row
  top, bot = 0, len(matrix)-1
  while top < bot:
    mid = (top + bot) // 2
    if target > matrix[mid][-1]:
      top = mid + 1
    elif target < matrix[mid][0]:
      bot = mid - 1
    else:
      top = bot = mid
  left, right = 0, len(matrix[bot])-1
  # Perform regular binary search
  while left <= right:
    mid = (left + right) // 2
    if target == matrix[bot][mid]:
      return True
    elif target < matrix[bot][mid]:
      right = mid - 1
    else:
      left = mid + 1
  return False

"""
Isolate to a single row using an adjusted binary search.
Then perform normal binary search on that single row.

Time Complexity: O(lgn + lgm)
Space Complexity: O(1)
"""

def search_2d_matrix(matrix: list[list[int]], target: int) -> bool:
  r, c = 0, len(matrix[0])-1
  while r < len(matrix) and c >= 0:
    num = matrix[r][c]
    if num == target:
      return True
    elif num > target:
      c -= 1
    else:
      r += 1
  return False