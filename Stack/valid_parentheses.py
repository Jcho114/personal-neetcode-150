"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

def isValid(s: str) -> bool:
  stack = []
  mapping = {')': '(', '}': '{', ']': '['}
  
  for c in s:
    if c in ['(', '{', '[']:
      stack.append(c)
    else:
      if not stack or mapping[c] != stack.pop():
        return False
      
  return len(stack) == 0

"""
We follow the logic provided in the prompt.

TC: O(n)
SC: O(n)
"""