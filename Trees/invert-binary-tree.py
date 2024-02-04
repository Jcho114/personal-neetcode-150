"""
226. Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
"""

from typing import Optional
from node import Node

def invert_binary_tree(root: Optional[Node]) -> Optional[Node]:
  if root:
    root.left, root.right = invert_binary_tree(root.right), invert_binary_tree(root.left)
  return root

"""
Used recursion to swap the left and right subtrees of each node

Time Complexity: O(n)
Space Complexity: O(n) if you consider the stack frame since its not tail recrusive
"""