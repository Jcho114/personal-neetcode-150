"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
"""

from typing import Optional
from node import Node

def maximum_depth(root: Optional[Node]) -> int:
  if root:
    return 1 + max(maximum_depth(root.left), maximum_depth(root.right))
  return 0

"""
Traverse through every node recursively with dfs.
Figure out which subtree has the maximum depth.
Add 1 to that depth and return the total depth.

Time Complexity: O(n)
Space Complexity: O(n) if you consider stack frames
"""