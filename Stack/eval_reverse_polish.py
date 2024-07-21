"""
150. Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""

from typing import List

def evalRPN(tokens: List[str]) -> int:
  stack = []
  opfuncs = {
    '+': lambda v1, v2: v1 + v2,
    '-': lambda v1, v2: v1 - v2,
    '*': lambda v1, v2: v1 * v2,
    '/': lambda v1, v2: int(v1 / v2)
  }

  for token in tokens:
    if token in ['+', '-', '*', '/']:
      v2, v1 = stack.pop(), stack.pop()
      stack.append(opfuncs[token](v1, v2))
    else:
      stack.append(int(token))
                
  return stack[-1]

"""
Store operands in stack, whenever we see an operator, we evaluate the
top two values in the stack then append it back into the stack.
Once we process all of the tokens we should end with the evaluated
value in the top of the stack.

TC: O(n)
SC: O(n)
"""