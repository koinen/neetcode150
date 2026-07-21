---
tags:
number: 11
title: Container With Most Water
url: https://leetcode.com/problems/container-with-most-water
difficulty: Medium
pattern: Two Pointers
status: solved
first-try: true
date-first-attempt: 2026-07-21
sr-due:
sr-interval: 1
sr-ease: 250
last-reviewed: 2026-07-21
---
## 1. Problem (in my own words)
Given an array of integers `heights`, find the most water it can contain within two walls of heights in `heights` and position being its' index. 
Example:
![[Container With Most Water Problem Illustration.png]]
This would return $7 \times 7 = 49$.
## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint               | Implication for approach |
| ------------------------ | ------------------------ |
| `2 <= n <= 10^5`         | up to $O(n \cdot log n)$ |
| `0 <= height[i] <= 10^4` | int32 is enough          |

## 3. Recognition trigger
You focus on choosing the best two indices.

## 4. Brute force

> [!info]- Idea
> Do a nested loop on every possible combination of containers, and take the max value.
---
>[!info]- Complexity 
>time $O(n^2)$ / space $O(1)$
---
> [!warning]- Why it's not enough?
> Always the same case, redundant work done repeatedly.

## 5. Optimal approach

> [!info]- Complexity 
>time $O(n)$ / space $O(1)$
---
> [!info]- Idea
> Use two pointers; start from the leftmost and rightmost. Since we know to get a bigger volume, you need more height, and only the smaller of the two is used. However, moving either pointer would reduce the volume since it will always reduce the width. Therefore, you just need to find more height, and compare the maximum up to now, until the pointers meet.
---
> [!info]- Why it works (the key insight)
> It works because the search is structured, and only the optimal choice is inspected (non-optimal choices being "there's no way this choice will ever beat the current one"). Keep the taller of the two, while the shorter one should move and find a taller wall.

## 6. Code
```python
# language: python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        ans = 0
        while l < r:
            ans = max(ans, (r - l)*min(height[r], height[l]))
            if height[l] >= height[r]:
                r -= 1
            else:
                l += 1
        
        return ans
```

## 7. Mistakes I actually made
- Was initially confused on how I should move the pointers; so I tried scrambling random rules until one clicked.

## 8. Edge cases to always check for this pattern
- [x] None

## 9. Related problems

---

### Flashcards