"""
973. K Closest Points to Origin

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane
and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance
(i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique
(except for the order that it is in).

Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted
"""

from collections import defaultdict
import heapq
import math

def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
  dct = defaultdict(list)
  for x,y in points:
    l = math.sqrt(pow(x,2) + pow(y,2))
    dct[l].append([x,y])
  heap = [l for l in dct.keys()]
  heapq.heapify(heap)
  res = []
  while len(res) < k:
    [res.append(el) for el in dct[heapq.heappop(heap)]]
  return res[:k]

"""
Pretty standard heap question.
You basically add to the heap lengths you calculated beforehand.
You then pop from the heap and then add the corresponding coordinates.
When you have a large enough list, you return it.

Time Complexity: O(nlgn)
Space Complexity: O(n)
"""