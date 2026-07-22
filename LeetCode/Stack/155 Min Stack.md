---
tags:
  - "#stack"
  - "#design"
number: 155
title: Min Stack
url: https://leetcode.com/problems/min-stack/
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
Design a stack data structure, with the usual `push()`, `pop()`, `top()` methods; but it can also get the minimum value inside the stack with `getMin()`.

## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                                                                                  | Implication for approach                                     |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| `-2^31 <= val <= 2^31 - 1`                                                                  | int32                                                        |
| Methods `pop`, `top` and `getMin` operations will always be called on **non-empty** stacks. | No need to handle empty stacks when those methods are called |
| At most `3 * 10^4` calls will be made to `push`, `pop`, `top`, and `getMin`.                | ~~Up to $O(n \cdot log n)$ time complexity~~                 |
| You must implement a solution with `O(1)` time complexity for each function.                | Well...                                                      |

## 3. Recognition trigger
Stack. it's on the name.
But fr though.
## 4. Brute force

> [!info]- Idea
> Keep an array form of the stack. If `getMin()` gets called, we just find the minimum from there.
---
>[!info]- Complexity 
>time $O(n)$ / space $O(n)$
---
> [!warning]- Why it's not enough?
> Because the problem asks for constant time complexity. Plus, the minimum values behaves the same as the actual stack, so why not make use of that? 

## 5. Optimal approach

> [!info]- Complexity 
>time $O(1)$ / space $O(n)$
---
> [!info]- Idea
> Use a second stack to store the minimum values. Only `push` and `pop` for the minimum values only. If the newly pushed element is less than or equal to the top of the minimum value stack, push it. Sync it too when `pop()` gets called. Compare the values, if they are equal, pop the minimum value stack as well. 
---
> [!info]- Why it works (the key insight)
> Because you've essentially stored it the same way as the actual stack, which has the time complexity of $O(1)$.

## 6. Code
```python
# language: python

from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()

    def push(self, value: int) -> None:
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        
        return

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

## 7. Mistakes I actually made
- I initially thought to keep the minimum value as just a variable. But quickly fell apart since it doesn't know which is its predecessor (which is the second least that can replace it). 

## 8. Edge cases to always check for this pattern
- [x] Don't forget to check if it's empty before checking top and popping.

## 9. Related problems
- None

---

### Flashcards