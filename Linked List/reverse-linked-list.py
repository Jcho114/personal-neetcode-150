"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []
"""

from typing import Optional
from node import Node

def reverse_linked_list(head: Optional[Node]) -> Optional[Node]:
  curr, prev = head, None
  while curr:
    temp = curr
    curr = curr.next
    temp.next = prev
    prev = temp
  return prev

"""
Basically using standard curr and prev pointers along with
a temp pointer.

Time Complexity: O(n)
Space Complexity: O(1)
"""