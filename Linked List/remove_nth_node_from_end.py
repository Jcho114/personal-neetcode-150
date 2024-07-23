"""
19. Remove Nth Node From End of List

Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

from typing import Optional
from node import Node

def removeNthFromEnd(head: Optional[Node], n: int) -> Optional[Node]:
  prev = curr = head
  for _ in range(n):
    curr = curr.next
        
  if curr is None:
    return head.next

  while curr.next:
    prev = prev.next
    curr = curr.next

  prev.next = prev.next.next
  return head

"""
Essentially, all we do is create an offset between two pointers.
One of the pointers point at the start of the list, the other
will point at the nth node.
We then increment the pointers till the farther node reaches the
end of the list.
Once we do that, the closer node is the node previous to the
target node. We then delete that node.
One edge case is if the target node is the head. We account
for that by checking of the further node is None. If it is,
we return the node after the head.

TC: O(n)
SC: O(1)
"""