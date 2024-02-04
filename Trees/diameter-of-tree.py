"""
543. Diameter of Binary Tree

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
"""

from typing import Optional
from node import Node

def diameter_of_tree(root: Optional[Node]) -> int:
  def length_of_subtree(curr: Optional[Node]) -> int:
    if curr:
      return 1 + max(length_of_subtree(curr.left), length_of_subtree(curr.right))
    return 0
  if root:
    return max(length_of_subtree(root.left) + length_of_subtree(root.right),
               diameter_of_tree(root.left), diameter_of_tree(root.right))
  return 0


"""
<Fix later since this Time Complexity is terrible>
"""