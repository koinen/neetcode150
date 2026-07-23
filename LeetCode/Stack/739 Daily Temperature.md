---
tags:
  - "#stack"
  - "#staff"
  - "#array"
  - "#monotonic-stack"
number: 739
title: Daily Temperature
url: https://leetcode.com/problems/daily-temperatures/
difficulty: Medium
pattern: Stack
status: solved
first-try: true
date-first-attempt: 2026-07-23
sr-due:
sr-interval: 1
sr-ease: 250
last-reviewed: 2026-07-23
---
## 1. Problem (in my own words)
Given an array of integers `temperatures` that describes the temperatures of sequential days, return an array `answer` such that `answer[i]` is the number of days to get a warmer temperature than the `i-th` day (`temperatures[i]`). If there are no future days where it's warmer, keep `answer[i]` as `0`.

Example:
`Input: temperatures = [73,74,75,71,69,72,76,73]`
`Output: [1,1,4,2,1,1,0,0]`

## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                         | Implication for approach                |
| ---------------------------------- | --------------------------------------- |
| `1 <= temperatures.length <= 10^5` | Up to $O(n \cdot logn)$ time complexity |
| `30 <= temperatures[i] <= 100`     | int32                                   |

## 3. Recognition trigger
I need the information of the **most recent** larger value up to now.

## 4. Brute force

> [!info]- Idea
> Loop through each element and find the closest larger value, also by scanning ahead.
---
>[!info]- Complexity 
>time $O(n^2)$ / space $O(1)$
---
> [!warning]- Why it's not enough?
> Because you're scanning the same things repeatedly. It's better if you can scan it once and store the information somehow.

## 5. Optimal approach

> [!info]- Complexity 
>time $O(n)$ / space $O(n)$
---
> [!info]- Idea
> Use a stack. Loop through the elements from behind, and store a decreasing stack (the top value will be less than the one below it). That way, if you ever need a larger value than the current top, just dig it. 
> Also, use the index and not the value, since the problem asks for the distance between indices.
---
> [!info]- Why it works (the key insight)
> Because you truly only need that particular information to proceed, right? This is keeping it as minimal as possible.

## 6. Code
```python
# language: python

from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        length = len(temperatures)
        ans = [0 for i in range(length)]
        for i in range(length-1, -1, -1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack: # else, skip and keep it as 0.
                ans[i] = stack[-1] - i
            stack.append(i)
        
        return ans
```

## 7. Mistakes I actually made
- Keep the index, instead of the values. The problem asks for indices is why.

## 8. Edge cases to always check for this pattern
- [x] Check stack empty or not before popping and peeking

## 9. Related problems
- 

---

### Flashcards