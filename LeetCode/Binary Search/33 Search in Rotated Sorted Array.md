---
tags:
number: 33
title: Search in Rotated Sorted Array
url: https://leetcode.com/problems/search-in-rotated-sorted-array/
difficulty: Medium
pattern: Binary Search
status: solved
first-try: true
date-first-attempt: 2026-07-26
sr-due:
sr-interval: 1
sr-ease: 250
last-reviewed: 2026-07-27
---
## 1. Problem (in my own words)
Basically [[153 Find Minimum in Rotated Sorted Array]]'s exact problem situation, except now instead of finding the minimum, you're told to search a value; and return its' position/index.

## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                                                      | Implication for approach                  |
| --------------------------------------------------------------- | ----------------------------------------- |
| You must write an algorithm with `O(log n)` runtime complexity. | b-b-bi...                                 |
| i'm not even gonna write down the `n` constraints anymore.      | because time complexity has been decided. |
| All values of `nums` are **unique**.                            | no need to handle duplicate cases         |
| `-10^4 <= nums[i] <= 10^4`                                      | i32 (oda level foreshadowing)             |

## 3. Recognition trigger
Search exact value in sorted array (even though it's rotated). It doesn't get more obvious than this.

## 4. Brute force

> [!info]- Idea
> Iterate through the array and compare it to the `target`.
---
>[!info]- Complexity 
>time $O(n)$ / space $O(1)$
---
> [!warning]- Why it's not enough?
> You need to use the fact that the array is sorted.

## 5. Optimal approach

> [!info]- Complexity 
>time $O(log n)$ / space $O(1)$
---
> [!info]- Idea
> Use [[153 Find Minimum in Rotated Sorted Array]] (make it return the index) to get your "effectively non-rotated sorted array", in which just do binary search on that thang.
---
> [!info]- Why it works (the key insight)
> Because.

## 6. Code
```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[l] <= nums[m]: 
                if nums[l] < nums[l-1]:
                    return l
                l = m + 1
            else:
                r = m

        return l

    def search(self, nums: List[int], target: int) -> int:
        x = self.findMin(nums)
        print(x)
        length = len(nums)
        l = 0
        r = length - 1
        
        while l <= r:
            m = (l + r) // 2
            rotated_m = (m + x) % length
            if nums[rotated_m] == target:
                return rotated_m
            elif nums[rotated_m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1
```

## 7. Mistakes I actually made
- 
- i don't even read one piece

## 8. Edge cases to always check for this pattern
- [x] no

## 9. Related problems
- 

---

### Flashcards