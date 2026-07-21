---
tags:
  - array
  - "#dynamic-programming"
  - "#two-pointers"
  - "#stack"
  - "#monotonic-stack"
number: 42
title: Trapping Rain Water
url: https://leetcode.com/problems/trapping-rain-water
difficulty: Hard
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
Given an array of non-negative integer `heights`, find out how many blocks of water (blue) that's trapped inside the structure of blocks (black) with heights of `heights`.

Example:
![[Trapping Rain Water Problem Illustration.png]]
Trapped water blocks = `6`.
## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint               | Implication for approach                 |
| ------------------------ | ---------------------------------------- |
| `1 <= n <= 2 * 10^4`     | Up to $O(n \cdot log n)$ time complexity |
| `0 <= height[i] <= 10^5` | int32                                    |

## 3. Recognition trigger
We need a quantity that depends on both left and right context, which in this case is the wall height.

## 4. Brute force

> [!info]- Idea
> Do a scan by the height value layer-by-layer (0, 1, 2, ...), and from that, try to get the fillable water blocks count by height by iterating over the heights.
---
>[!info]- Complexity 
>time $O(n \cdot m)$ / space $O(1)$
>$m$ is the maximum value of `height[i]`
---
> [!warning]- Why it's not enough?
> Because you shouldn't try to iterate over the values, it's redundant because you can just go to the next height value in `heights`. 

## 5. Optimal approach

> [!info]- Complexity 
>time $O(n)$ / space $O(1)$
---
> [!info]- Idea
> An optimization of the brute force approach, where we use two pointers to get the next height. Find the minimum wall height of the two pointers, just like [[11 Container With Most Water]], and fill the whole space with water. Subtract it later with the incoming blocks heights. And just move the pointers like [[11 Container With Most Water]].
---
> [!info]- Why it works (the key insight)
> Because now, you don't waste the effort on scanning the height layer-by-layer, but you already know the exact height and width you need to fill in.

## 6. Code
```python
# language: python

class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        ans = 0
        last_h = 0
        while l < r:
            curr_h = min(height[l], height[r])
            if curr_h > last_h:
                # print(f"found trench of height {curr_h}, adding {curr_h - last_h} * {(r - l - 1)}")
                ans += (curr_h - last_h) * (r - l - 1)
                last_h = curr_h
            if height[l] <= height[r]:
                l += 1
                ans -= min(last_h, height[l])
                # print(f"moving left: subtracting min({last_h}, {height[l]})")
            else:
                r -= 1
                ans -= min(last_h, height[r])
                # print(f"moving right: subtracting min({last_h}, {height[r]})")
        
        return ans + last_h # oversubtraction when l = r
```

## 7. Mistakes I actually made
- None bwoahahaha

## 8. Edge cases to always check for this pattern
- [ ] Off-by-one 

## 9. Related problems
- [[11 Container With Most Water]]

---

### Flashcards