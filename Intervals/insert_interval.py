"""
57. Insert Interval

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.
"""

from typing import List

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
  res = []

  for i in range(len(intervals)):
    start, end = intervals[i]
    if end < newInterval[0]:
      res.append([start, end])
    elif start > newInterval[1]:
      res.append(newInterval)
      return res + intervals[i:]
    else:
      newInterval = [
        min(newInterval[0], start),
        max(newInterval[1], end)
      ]
        
  res.append(newInterval)
  return res

"""
Not much to say about it, just trying to make the code concise was a bit of a
headache.

TC: O(n)
SC: O(n)
"""