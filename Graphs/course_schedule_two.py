"""
210. Course Schedule II

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
"""

from typing import List
from collections import deque

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
  degrees = [0]*numCourses
  adj = [[] for _ in range(numCourses)]

  for dest, src in prerequisites:
    degrees[dest] += 1
    adj[src].append(dest)
        
  queue = deque([node for node in range(numCourses) if degrees[node] == 0])
  ordering = []
  while queue:
    node = queue.popleft()
    ordering.append(node)
    for dest in adj[node]:
      degrees[dest] -= 1
      if degrees[dest] == 0:
        queue.append(dest)
        
  return ordering if len(ordering) == numCourses else []

"""
Here we used Kahn's Topological Sorting Algorithm

TC: O(V+E)
SC: O(V+E)
"""