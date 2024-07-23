"""
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""


from collections import defaultdict

def characterReplacement(s: str, k: int) -> int:
  counts = defaultdict(int)
  l = mfreq = 0
  for r in range(len(s)):
    counts[s[r]] += 1
    mfreq = max(mfreq, counts[s[r]])
    if r - l + 1 - mfreq > k:
      counts[s[l]] -= 1
      l += 1
  return r - l + 1

"""
Have a sliding window that starts at length 0 but increases by 1
whenever we can replace enough characters to have a repeating character
substring in the given window. We can do this replacement if the length
of the window subtracted by the highest frequent character count is
at most k. We keep track of the most frequent character count by using
a dictionary that contains all of the character frequencies in a given
window.
TC: O(n)
SC: O(n)
"""