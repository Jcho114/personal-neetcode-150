"""
133. Clone Graph

Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
"""

from typing import Optional
from node import Node

def clone_graph(node: Optional[Node]) -> Optional[Node]:
  clones = { None: None }

  def clone(curr):
    if curr:
        clones[curr] = Node(curr.val)
        for neighbor in curr.neighbors:
            if neighbor not in clones:
                clone(neighbor)
            clones[curr].neighbors.append(clones[neighbor])

  clone(node)
  return clones[node]

"""
Akin to a preorder traversal for trees, you first build the current node, then
recursively build and attach all of the node's neighbors. However, since this
is a graph, we need to maintain references of these nodes since neighbors are
not deterministic like a tree. To elaborate, a tree always have left and right
pointers that we only need to attach once to the parent node. For the graph, however,
we have an arbitrary amount of neighbors, those of which might be connected
to more than one node. As a result, we use a dictionary that also serves
as a visited set.

TC: O(V+E)
SC: O(V)
"""