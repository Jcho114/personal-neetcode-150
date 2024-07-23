"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

from typing import Optional
from node import Node

def addTwoNumbers(l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:
  dummy = Node(-1)
        
  curr = dummy
  carry = 0
  while l1 and l2:
    val = (l1.val + l2.val + carry) % 10
    carry = (l1.val + l2.val + carry) // 10
    curr.next = Node(val)
    curr = curr.next
    l1 = l1.next
    l2 = l2.next
        
  while l1:
    val = (l1.val + carry) % 10
    carry = (l1.val + carry) // 10
    curr.next = Node(val)
    curr = curr.next
    l1 = l1.next
        
  while l2:
    val = (l2.val + carry) % 10
    carry = (l2.val + carry) // 10
    curr.next = Node(val)
    curr = curr.next
    l2 = l2.next

  if carry:
    curr.next = Node(carry)
        
  return dummy.next

"""
We basically simulate what we did way back in kindergarten.

TC: O(max(n, m))
SC: O(max(n, m))
"""