"""
143. Reorder List

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
"""

from typing import Optional

class Node:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def reorder_list(head: Optional[Node]) -> None:
  nodes = []
  curr = head
  while curr:
    nodes.append(curr)
    curr = curr.next
  l, r = 0, len(nodes)-1
  while l <= r:
    if l < r:
      if nodes[l].next != nodes[r]:
        nodes[r].next = nodes[l].next
      else:
        nodes[r].next = None
      nodes[l].next = nodes[r]
    else:
      nodes[l].next = None
    l += 1
    r -= 1
  return head

"""
<Finish writeup later>

Time Complexity: O(n)
Space Complexity: O(n)
"""