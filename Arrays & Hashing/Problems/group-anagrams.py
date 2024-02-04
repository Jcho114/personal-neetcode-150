"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""

def group_anagrams(strs: list[str]) -> list[list[str]]:
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  # Return number of occurences of each character in a str
  def convert_to_anagram(s):
    res = [0]*26
    for c in s:
      res[alphabet.find(c)] += 1
    # Convert to tuple so that value is hashable
    return tuple(res)
  res = {}
  for s in strs:
    converted = convert_to_anagram(s)
    # Add string to associated anagram bucket
    if converted not in res:
      res[converted] = []
    res[converted].append(s)
  return res.values()

"""
Use a dictionary to store the anagram "buckets"
Use helper function to convert strs to associated occurence table
Occurence table is basically just an array of all the occurences of
each character for a string
Iterate through the elements, and add each element to their associated
bucket using occurence tables
Return the list of buckets after iterating through the input list

Time Complexity: O(n*m)
Space Complexity: O(n*m)
"""