---
tags:
  - "#binary-search"
  - array
number: 704
title: Binary Search
url: https://leetcode.com/problems/binary-search/
difficulty: Easy
pattern: Binary Search
status: solved
first-try: true
date-first-attempt: 2026-07-25
sr-due:
sr-interval: 1
sr-ease: 250
last-reviewed: 2026-07-25
---
## 1. Problem (in my own words)
Given a sorted (ascending) array of integers, find the index of the `target` if it exists in the array, else return `-1`.

## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                                                      | Implication for approach                    |
| --------------------------------------------------------------- | ------------------------------------------- |
| `1 <= nums.length <= 10^4`                                      | ~~Up to $O(n^2)$~~                          |
| `-10^4 < nums[i], target < 10^4`                                | int32, whatever                             |
| All the integers in `nums` are **unique**.                      | No need to think about duplicate edge cases |
| You must write an algorithm with `O(log n)` runtime complexity. | well..                                      |

## 3. Recognition trigger
Finding an element in a sorted array.

## 4. Brute force

> [!info]- Idea
> Scan through and find it
---
>[!info]- Complexity 
>time $O(n)$ / space $O(1)$
---
> [!warning]- Why it's not enough?
> Because the problem wants $O(log n)$ complexity. Maybe make use of the fact that it's sorted..?

## 5. Optimal approach

> [!info]- Complexity 
>time $O(log n)$ / space $O(1)$
---
> [!info]- Idea
> Use [[Binary Search|binary search]].
---
> [!info]- Why it works (the key insight)
> Because. 

## 6. Code
```python
# language: python

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1 
```

## 7. Mistakes I actually made
- Use python's `//` to get integer division

## 8. Edge cases to always check for this pattern
- [x] `l <= r` or `l < r`.

## 9. Related problems
- 

---

### Flashcards
