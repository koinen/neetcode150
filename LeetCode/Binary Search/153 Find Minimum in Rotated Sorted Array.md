---
tags:
number: 153
title: Find Minimum in Rotated Sorted Array
url: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
difficulty: Medium
pattern: Binary Search
status: solved
first-try: true
date-first-attempt: 2026-07-26
sr-due:
sr-interval: 1
sr-ease: 250
last-reviewed: 2026-07-26
---
## 1. Problem (in my own words)
Given an array of integers `arr`, in which it has been sorted in a non-descending order. However, it got rotated. Find the minimum value.

Rotated is when you translate the indices, for example:
Original: `[0, 1, 2, 3, 4, 5, 6, 7]`
Rotated: `[5, 6, 7, 0, 1, 2, 3, 4]`

## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                                                | Implication for approach                 |
| --------------------------------------------------------- | ---------------------------------------- |
| `1 <= n <= 5000`                                          | ~~$O(n^2 \cdot log n)$ time complexity~~ |
| All the integers of `nums` are **unique**.                | no need to handle duplicate cases        |
| You must write an algorithm that runs in `O(log n) time`. | b-b-b-binary search...?!                 |

## 3. Recognition trigger
$O(log n)$ time complexity. Sorted.

## 4. Brute force

> [!info]- Idea
> Scan through the array and find the minimum.
---
>[!info]- Complexity 
>time $O(n)$ / space $O(1)$
---
> [!warning]- Why it's not enough?
> You need to use the fact that it's sorted, even though it's rotated.

## 5. Optimal approach

> [!info]- Complexity 
>time $O(log n)$ / space $O(1)$
---
> [!info]- Idea
> Use binary search. However, you can't really apply it to the problem directly. Use the fact that it's sorted, and therefore if `arr[left] > arr[mid]`, the 'jump' from the rotation is in there; else, it's on the other half; or it could be that there's no rotation at all.
---
> [!info]- Why it works (the key insight)
> Because you can think of the array segments as non-rotated or rotated, which results in a more digestible to use binary search on. `[1,1,1,1,0,0,0,0,0]` where `1` represents rotated (WLOG). And you just need to return the boundary between `1` and `0`.

## 6. Code
```python
# language: python

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            # print(f"new l-r={l}-{r}: m={m}")
            if nums[l] <= nums[m]: # this is proper, no rotation in here, which means, we need to chop it down. either that; or this is the actual minimum.
                if nums[l] < nums[l-1]:
                    # print("returning early...")
                    return nums[l]
                l = m + 1
            else:
                r = m
        #              m
        #  0  1  2  3  4  5  6  7  8  9
        # [8, 9, 0, 1, 2, 3, 4, 5, 6, 7]
        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        return nums[l]
```

## 7. Mistakes I actually made
- I checked the whether this segment is rotated or not by comparing left and right; which defeats the whole purpose. I only need to check one half, if it's rotated check here; if not check the other half.
- Knowing when to use `l <= r`, or `l < r`. Check [[binary search]] for the details.

## 8. Edge cases to always check for this pattern
- [ ] Handle if array isn't rotated (Fortunately python can do `[-1]`, which loops back and accesses the end of the array, so I don't have to explicitly handle it, haha)

## 9. Related problems
- [[33 Search in Rotated Sorted Array]]

---