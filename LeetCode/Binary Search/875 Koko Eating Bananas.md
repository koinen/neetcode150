---
tags:
number: 875
title: Koko Eating Bananas
url: https://leetcode.com/problems/koko-eating-bananas/
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
Find the minimum possible answer `k`, so that Koko can finish all her banana piles in `h` hours.
For example:
`piles = [3,6,7,11], h = 8` 
if `k = 2`, 
first pile would take 2 hours to finish; second 3; third 4; fifth 6; a total of 15 hours, which is more than `h`, so `k = 2` is not a valid answer. The answer would be `k = 4`.

## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                  | Implication for approach                                      |
| --------------------------- | ------------------------------------------------------------- |
| `1 <= piles.length <= 10^4` | Up to $O(n^2)$ time complexity                                |
| `piles.length <= h <= 10^9` | `h` is always valid, no need to handle cases where `h` isn't. |
| `1 <= piles[i] <= 10^9`     | int32                                                         |

## 3. Recognition trigger
"Find the minimum/maximum answer that satisfies condition X.", in which case it has to satisfy the resulting `h` has to be less than the target `h`. 

## 4. Brute force

> [!info]- Idea
> Try `k` values one by one.
---
>[!info]- Complexity 
>time $O(n * m)$ / space $O(1)$
>`m` is `max(piles[i])` 
---
> [!warning]- Why it's not enough?
> Because, you're essentially doing a search on a sorted space. Your `k` search is trying values one-by-one, and the resulting `h` decreases monotonically, too.

## 5. Optimal approach

> [!info]- Complexity 
>time $O(n \cdot log n)$ / space $O(1)$
---
> [!info]- Idea
> Use [[Binary Search on Answer|binary search on the answer]]. 
---
> [!info]- Why it works (the key insight)
> Because, the resulting solution space will basically look like `[0,0,0,0,1,1,1,1,...]` where 0 represent the invalid answers, and 1 the valid ones. We just need to find the boundary between 0 and 1, and return it.

## 6. Code
```python
# language: python

class Solution:
    def checkHours(self, k):
        totalHours = 0
        for pile in self.piles:
            totalHours += (pile + k - 1) // k
        # print(f"k={k}, totalHours={totalHours}")
        return totalHours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # solution space:
        #  3   4  5  6  7  8  9  10 11
        # [10, 8, 8, 6, 5, 5, 5, 5, 4]
        self.piles = piles
        l = 1
        r = max(piles)
        ans = -1
        while l <= r:
            m = (l + r) // 2
            # print(f"\nm: {m}")
            if self.checkHours(m) <= h: # 1, acceptable.
                ans = m
                # print(f"acceptable answer, chopping down right half")
                r = m - 1
            else:
                # print(f"non-acceptable answer, chopping down left half")
                l = m + 1
        
        return ans
        # pass
```

## 7. Mistakes I actually made
- [[binary search|Binary search on answer]] has a different mechanism, since it needs to store the answer and keep searching, not just return when it finds the exact match (of satisfying the condition).  
- Didn't know how to effectively use `ceil` (without actually using `math.ceil`)

## 8. Edge cases to always check for this pattern
- [ ] Knowing when to use `l <= r`, or `l < r`. Check [[binary search]] for the details.

## 9. Related problems
- 

---