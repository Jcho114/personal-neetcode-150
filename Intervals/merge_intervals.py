"""
56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all
overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.
"""

from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
  res = []
  intervals = sorted(intervals)
  res.append(intervals[0])

  for start, end in intervals[1:]:
    if start > res[-1][1]:
      res.append([start, end])
    else:
      res[-1][1] = max(res[-1][1], end)
        
  return res

"""
We first sort the intervals by their start value then end value.
We now stage the first interval to a new list, then check if any
following intervals can merge with it. If so, we update the staged
interval. If not, we stage that next interval to the new list, etc.

TC: O(n)
SC: O(n)
"""