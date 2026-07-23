---
tags:
  - stack
  - array
  - "#math"
number: 150
title: Evaluate Reverse Polish Notation
url: https://leetcode.com/problems/evaluate-reverse-polish-notation
difficulty: Medium
pattern: Stack
status: solved
first-try: true
date-first-attempt: 2026-07-22
sr-due:
sr-interval: 1
sr-ease: 250
last-reviewed: 2026-07-22
---
## 1. Problem (in my own words)
Given an array of strings (tokens) that describes an expression using the postfix notation, return the result of the expression.
The type of strings entered include:
- Numbers (`"0", "10", "109", ...`)
- Operator (`"*", "/", "+", "-"`)
## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                                                                                                                                                    | Implication for approach       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| `1 <= tokens.length <= 10^4`                                                                                                                                  | Up to $O(n^2)$ time complexity |
| No division by zero.                                                                                                                                          | Great. No need to handle this  |
| - Number inputs will be integers in the range `[-200, 200]`<br>- The answer and all the intermediate calculations can be represented in a **32-bit** integer. | int32 is enough                |

## 3. Recognition trigger
The most basic expression is `numLeft, numRight, operator`. Operator needs the top **two most recent** numbers. Gee I wonder what's the most effective way to get the **top most recent** values.

## 4. Brute force
I don't know. The use of stack is already etched to my brain for this problem.

## 5. Optimal approach

> [!info]- Complexity 
>time $O(n)$ / space $O(n)$
---
> [!info]- Idea
> Use stack to keep the numbers. Pop the two numbers if an operator is found, calculate the result, and push it back in. The result would be just one value in the stack at the end of the expression.
---
> [!info]- Why it works (the key insight)
> Because it's always two numbers and an operator at the most basic level. 

## 6. Code
```python
# language: python

from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for i in range(len(tokens)):
            if tokens[i] == '+' or tokens[i] == '*' or tokens[i] == '-' or tokens[i] == '/' :
                num_r = stack.pop()
                num_l = stack.pop()
                if tokens[i] == '+':
                    # print(f"{num_l} + {num_r} = {num_l + num_r}")
                    stack.append(num_l + num_r)
                elif tokens[i] == '/':
                    # print(f"{num_l} / {num_r} = {int(num_l / num_r)}")
                    stack.append(int(num_l / num_r))
                elif tokens[i] == '-':
                    # print(f"{num_l} - {num_r} = {num_l - num_r}")
                    stack.append(num_l - num_r)
                else:
                    # print(f"{num_l} * {num_r} = {num_l * num_r}")
                    stack.append(num_l * num_r)
            else:
                stack.append(int(tokens[i]))
        
        return stack.pop()
```

## 7. Mistakes I actually made
- The division i used earlier, with the operator `//` in Python doesn't converge to zero if it's negative. The use of `int(num_l / num_r)` fixes that.

## 8. Edge cases to always check for this pattern
- [x] Nothing to check for this particular problem

## 9. Related problems
- None

---

### Flashcards