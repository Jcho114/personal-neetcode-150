"""
138. Copy List with Random Pointer

A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

Your code will only be given the head of the original linked list.
"""

from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head: Optional[Node]) -> Optional[Node]:
  clones = { None: None }

  def clone(curr):
    if curr:
      new = Node(curr.val)
      clones[curr] = new
      if curr.next not in clones:
        clone(curr.next)
      if curr.random not in clones:
        clone(curr.random)
      new.next = clones[curr.next]
      new.random = clones[curr.random]

  clone(head)
  return clones[head]

"""
We have a clone function that will always fully clone its
argument curr and save it in a clones dictionary. Knowing
this, all we have to do to maintain that assumption is to
first save a reference of a new node to the dictionary, then
recursively clone any of the next and random nodes if they
are not in the dictionary, then assign those clones to
our curr and random fields, respectively.

TC: O(n)
SC: O(n)
"""