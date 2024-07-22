"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring
without repeating characters.
"""

def lengthOfLongestSubstring(s: str) -> int:
  last_seen = {}
  l = res = 0

  for r, c in enumerate(s):
    if c in last_seen and last_seen[c] >= l:
      l = last_seen[c] + 1
    last_seen[c] = r
    res = max(res, r - l + 1)

  return res

"""
We have a sliding window that will always be a substring
without repeating characters. To help us do that we will
use a dictionary storing the index of where we last saw
a character. With this, we can tell if we already saw a
character in our current window, meaning that we should
shift the left side of the window forward until there are
no repeated characters. We also keep track of the longest
length by using a variable that we return once we iterate
through all of the characters.

TC: O(n)
SC: O(1)
"""