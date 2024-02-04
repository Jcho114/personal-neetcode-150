"""
100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
"""

from typing import Optional
from node import Node

def same_tree(p: Optional[Node], q: Optional[Node]) -> bool:
  if p and q:
    return p.val == q.val and same_tree(p.left, q.left) and same_tree(p.right, q.right)
  return not p and not q

"""
Recursively traverse through both trees in the same fashion.
Check if each node's values are correct.
Also check if each tree follows the same structure.
If all checks pass, return True.
Otherwise, return False.

Time Complexity: O(min(n, m)) = O(n)
Space Complexity: O(min(n, m)) = O(n)
"""