"""
703. Kth Largest Element in a Stream

Design a class to find the kth largest element in a stream. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the
stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element
representing the kth largest element in the stream.

Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
"""

import heapq

# View a min-heap of length k as a collection of the top-k elements
# heap[0] will then be the kth largest element
class KthLargest:
  # Time Complexity: O(nlgn)
  # Space Complexity: O(n)
  def __init__(self, k: int, nums: list[int]):
    self.heap = nums
    self.k = k
    heapq.heapify(self.heap)
    while len(self.heap) > k:
        heapq.heappop(self.heap)

  # Time Complexity: O(lgn)
  def add(self, val: int) -> int:
    heapq.heappush(self.heap, val)
    if len(self.heap) > self.k:
      heapq.heappop(self.heap)
    return self.heap[0]