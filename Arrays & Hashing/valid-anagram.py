"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""

def valid_anagram(s, t):
  chs = {}
  # Increment every instance of a character in the dict
  for c in s:
    if c not in chs:
      chs[c] = 0
    chs[c] += 1
  # Decrement every instance of a character in the dict
  for c in t:
    if c not in chs:
      chs[c] = 0
    chs[c] -= 1
  # If all the dict values are 0, return True
  # Otherwise, return false
  for count in chs.values():
    if count != 0:
      return False
  return True

"""
Use a dictionary to keep count of all the occurences for each character
First increment every occurrence of a character in string s
Then decrement for string t
If the dictionary only contains 0s for its values, the s is an anagram of t
Otherwise, it is not

Time Complexity: O(n)
Space Complexity: O(n) if one of s and t includes distinct characters
"""