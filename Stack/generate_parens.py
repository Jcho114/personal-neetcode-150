"""
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

from typing import List

def generateParenthesis(n: int) -> List[str]:
  res = []

  def build(l, r, s):
    if l == 0:
      res.append(s+")"*r)
    elif l == r:
      build(l-1, r, s+"(")
    else:
      build(l-1, r, s+"(")
      build(l, r-1, s+")")

  build(n, n, "")
  return res

"""
Not sure what this has to do with stacks.
With that said, though, the way I approached this problem was with backtracking.
I first noticed a decision tree pattern, which was that, given that we start with
n opening and n closing parens, if we have the same amount of opening and closing
braces, we need to add an opening brace, if we have more closing braces, we can
either add an opening or closing brace, and if we don't have any opening brances,
we have to add our remaining closing braces.

TC: Not sure, but probs exponential
SC: Not sure, but probs exponential
"""