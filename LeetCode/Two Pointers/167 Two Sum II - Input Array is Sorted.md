---
tags:
  - array
  - two-pointers
number: 167
title: Two Sum II - Input Array is Sorted
url: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
difficulty: Medium
pattern: Two Pointers
status: solved
first-try: true
date-first-attempt: 2026-07-20
sr-due:
sr-interval: 1
sr-ease: 250
last-reviewed: 2026-07-20
---
## 1. Problem (in my own words)
Basically [[1 Two Sum]], but array is already sorted. Also, the **array is 1-indexed**, for whatever reason.

## 2. Constraints & what they imply
<!-- e.g. n ≤ 10^5 → need O(n log n) or better. n ≤ 20 → bitmask/brute force is fine. -->
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                                                     | Implication for approach                                                     |
| -------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `2 <= numbers.length <= 3 * 10^4`                              | Up to $O(n \cdot log n)$ time complexity; $O(n^2)$ is a no-no.               |
| - `-1000 <= numbers[i] <= 1000`<br>- `-1000 <= target <= 1000` | no need for int64, int32 is enough                                           |
| $O(1)$ extra space                                             | No hash tables.                                                              |
| Only one solution exists                                       | No need to handle choosing solutions if more than one exists or none exists. |

## 3. Recognition trigger
It's sorted. One of the prerequisites for using two pointers. Plus, it's explicitly stated that we need two indices.

## 4. Brute force
[[1 Two Sum#4. Brute force|Two Sum's brute force]], except it's not enough now, because we need to make use of the sorted order.

## 5. Optimal approach

> [!info]- Complexity 
>time $O(n)$ / space $O(1)$
---
> [!info]- Idea
> Have two pointers, the usual; left and right;
> Since the array is sorted, we can make use of it by slowly moving the pointers. 
> 1. First; check if the sum of those pointers equals to the `target`. 
> 	If it does, just return. 
> 	If it doesn't, check if it's less or more than the `target`. 
> 		If it's less, that means we need to move the left pointer, increase the sum.
> 		If it's more, we overshot. we need to move the right pointer, reducing the sum.
> 2. Rinse and repeat
---
> [!info]- Why it works (the key insight)
> Because we know the solution exists, we just need to adjust the pointers to get it as close to the `target` as possible. The sorted order made it easy for what to do.

## 6. Code
```python
# language: python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            res = numbers[l] + numbers[r]
            if (res == target):
                return [l+1, r+1]
            if (res > target):
                r -= 1
            if (res < target):
                l += 1
        
        return [0,0] # technically unreachable, just a safety net 
```

## 7. Mistakes I actually made
- None

## 8. Edge cases to always check for this pattern
- [ ] Be careful on deciding if it's `l < r` or `l <= r`.

## 9. Related problems
- [[1 Two Sum]]

---

### Flashcards