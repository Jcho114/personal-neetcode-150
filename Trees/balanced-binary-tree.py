"""
110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

A height-balanced binary tree is a binary tree in which the depth of
the two subtrees of every node never differs by more than one.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
"""

from typing import Optional
from node import Node

def balanced_binary_tree(root: Optional[Node]) -> bool:
  def height(curr: Optional[Node]) -> int:
    if curr:
      return max(height(curr.left), height(curr.right)) + 1
    return 0
  if root:
    return abs(height(root.left) - height(root.right)) <= 1 and balanced_binary_tree(root.left) and balanced_binary_tree(root.right)
  return True

"""
Currently using naive approach, will optimize later...
Current issue is that we are repeating node visits
Probably going to have to use some bottom up approach where I change the return type
"""