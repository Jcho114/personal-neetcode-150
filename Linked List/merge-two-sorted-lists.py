"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""

from typing import Optional

class Node:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def merge_two_sorted_lists(list1: Optional[Node], list2: Optional[Node]) -> Optional[Node]:
  # case where only list1 exists
  if list1 and not list2:
    return list1
  # case where only list2 exists
  if not list1 and list2:
    return list2
  curr1, curr2 = list1, list2
  res = builder = None
  # when both list nodes exist
  while curr1 and curr2:
    if curr1.val <= curr2.val:
      if not res:
        res = builder = curr1
      else:
        builder.next = curr1
        builder = builder.next
      curr1 = curr1.next
    else:
      if not res:
        res = builder = curr2
      else:
        builder.next = curr2
        builder = builder.next
      curr2 = curr2.next
  # when one list still has nodes left
  if builder:
    builder.next = curr1 if curr1 else curr2
  return res

"""
I basically had two pointers that traversed both lists.
I compared the two node values so that the smaller one is added to
the result list and is traversed by their corresponding pointer.
If one list is longer than the other I add the remaining sublist
to the result list once I finish traversing the other list.
If one of the lists is empty, I just returned the head of the
other list.

Time Complexity: O(n + m)
Space Complexity: O(1)
"""