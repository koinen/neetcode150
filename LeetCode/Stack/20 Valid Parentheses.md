---
tags:
  - "#stack"
  - "#string"
number: 20
title: Valid Parentheses
url: https://leetcode.com/problems/valid-parentheses
difficulty: Easy
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
Return `true` if a string `s` is a valid expression of parentheses. Else, false.
Parentheses characters only consists of `'(', ')', '[', ']', '{', '}'`.

## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint              | Implication for approach |
| ----------------------- | ------------------------ |
| `1 <= s.length <= 10^4` | Up to $O(n^2)$           |

## 3. Recognition trigger
You only need to see the information about last/most recent open parentheses in the string to proceed.

## 4. Brute force

I can't think of a "brute force" approach without using the stack.

## 5. Optimal approach

> [!info]- Complexity 
>time $O(n)$ / space $O(n)$
---
> [!info]- Idea
> Use stack to keep track of the last/most recent open parentheses, only pop when you found a close parentheses. Also, they have to match (`'(' with ')', etc.`)
---
> [!info]- Why it works (the key insight)
> Because you keep the information to proceed at the minimum.

## 6. Code
```python
# language: python

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        i = 0
        parentheses = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        while i < len(s):
            if s[i] in parentheses.values():
                stack.append(s[i])
            elif stack:
                top = stack.pop()
                if top != parentheses[s[i]]:
                    return False
            else:
                return False
            i += 1

        if stack:
            return False
            
        return True
```

## 7. Mistakes I actually made
- None
## 8. Edge cases to always check for this pattern
- [x] Don't forget to check if stack is empty or not at the end.
- [x] Don't forget to check if stack is empty or not before popping.

## 9. Related problems
- None

---

### Flashcards