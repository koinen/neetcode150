---
tags:
number: 84
title: Largest Rectangle in Histogram
url: https://leetcode.com/problems/largest-rectangle-in-histogram
difficulty: Hard
pattern: Stack
status: solved-with-solution
first-try:
date-first-attempt: 2026-07-24
sr-due:
sr-interval: 1
sr-ease: 250
last-reviewed: 2026-07-25
---
## 1. Problem (in my own words)
Given an array of integers `heights` that represents the heights in a histogram, find the maximum area of rectangle the can be formed in it.

## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                    | Implication for approach |
| ----------------------------- | ------------------------ |
| `1 <= heights.length <= 10^5` | Up to $O(n \cdot log n)$ |
| `0 <= heights[i] <= 10^4`     | int64 for the answer     |

## 3. Recognition trigger
>When the answer depends on the nearest boundary-breaking element in one or both directions, and brute-force involves rescanning outward per index → monotonic stack, because the stack lets you re-derive both boundaries from the pop event itself, encoding order without recomputation.
## 4. Brute force

> [!info]- Idea
> Find all the rectangles that can be formed, by scanning through every possible element
---
>[!info]- Complexity 
>time $O(n^2)$ / space $O(1)$
---
> [!warning]- Why it's not enough?
> Because you're not using the memory, and you keep scanning the same element over and over again.

Optimized
> [!info]- Idea
> Find the left and right boundary of each height. Scan left and right until you find a shorter height or when you've hit the end of the array.
---
>[!info]- Complexity 
>time $O(n^2)$ / space $O(1)$
---
> [!warning]- Why it's not enough?
> Even though you're only inspecting the best candidates, since you've get the maximum width for every height, you're still scanning through the same elements again and again. Make use of the memory to keep the information there. 

## 5. Optimal approach

> [!info]- Complexity 
>time $O(n)$ / space $O(n)$
---
> [!info]- Idea
> Use a stack and keep it monotonic. If you've found a shorter element, you have found the right boundary for the current height (top of the stack). For the left boundary, you can use the previous element in the stack. 
---
> [!info]- Why it works (the key insight)
> Because. You effectively only scan the element once, no redundant operations needed.

## 6. Code

Stack but didn't think I was able to get the left and right boundary at once.
```python
# language: python

from collections import deque

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque()

        rightmost = [0 for i in range(len(heights))]
        leftmost = [0 for i in range(len(heights))]
        
        length = len(heights)

        for i in range(length):
            while stack and heights[i] < heights[stack[-1]]:
                last = stack.pop()
                rightmost[last] = i
            stack.append(i)
        
        while stack:
            last = stack.pop()
            rightmost[last] = length

        for i in range(length-1, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                last = stack.pop()
                leftmost[last] = i
            stack.append(i)
        
        while stack:
            last = stack.pop()
            leftmost[last] = -1

        # print(leftmost)
        # print("=================")
        # print(rightmost)
        ans = 0
        for i in range(length):
            ans = max(ans, (rightmost[i] - leftmost[i] - 1)*heights[i])
        
        return ans
```

Optimal
```python
# language: python

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        length = len(heights)

        ans = 0
        for i in range(length + 1):
            h = heights[i] if i < length else -1 # whatever value to trigger the h < heights[stack[-1]] check
            while stack and h < heights[stack[-1]]:
                top = stack.pop()
                left = -1 if not stack else stack[-1]
                width = i - left - 1
                ans = max(ans, width * heights[top])
            stack.append(i)
        
        return ans
```

## 7. Mistakes I actually made
- Not really a mistake, but a miss for optimization; but you can get both boundaries with a single pass.

## 8. Edge cases to always check for this pattern
- [x] You have make sure to empty the stack, to cover all the possible solutions

## 9. Related problems

---

### Flashcards