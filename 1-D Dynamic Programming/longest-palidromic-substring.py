"""
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""

def longest_palindrome(s: str) -> str:
  res = ""
  res_count = 0
  for i in range(len(s)):
    l, r = i, i
    while l >= 0 and r < len(s) and s[l] == s[r]:
        if r - l + 1 > res_count:
            res = s[l:r+1]
            res_count = r - l + 1
            l -= 1
            r += 1
        l, r = i, i+1
    while l >= 0 and r < len(s) and s[l] == s[r]:
        if r - l + 1 > res_count:
            res = s[l:r+1]
            res_count = r - l + 1
        l -= 1
        r += 1
    return res
  
"""
We are basically considering the i in the iterations as the "center" of a
string. We then use l and r to check for palindromes. Since palindromes can
be even and odd, we perform this check twice with different ls and rs.

Time Complexity: O(n^2)
Space Compelxity: O(1)
"""