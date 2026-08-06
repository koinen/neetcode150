---
tags:
  - array
  - dynamic-programming
number: 121
title: Best Time to Buy and Sell Stock
url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
difficulty: Easy
pattern: Sliding Window
status: solved
first-try: true
date-first-attempt: 2026-08-06
---
## 1. Problem (in my own words)
Given an array of integers `nums` find the maximum value of `nums[r] - nums[l]`, where `r >= l`.

## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                 | Implication for approach |
| -------------------------- | ------------------------ |
| `1 <= nums.length <= 10^5` | $O(n \cdot log n)$       |

## 3. Recognition trigger
I don't know.... it's like I'm forcing it--cuz I already know it's a sliding window problem based on the roadmap. I mean the problem itself doesn't have sliding window tag?? 

## 4. Brute force

> [!info]- Idea
> Iterate through every possible `l` and `r`-s.
---
>[!info]- Complexity 
>time $O(n^2)$ / space $O(1)$
---
> [!warning]- Why it's not enough?
> Because you're continuing on dead paths that's never going to be the answer.

## 5. Optimal approach

> [!info]- Complexity 
>time $O(n)$ / space $O(1)$
---
> [!info]- Idea
> Use sliding window, left signifies the buy value, right pointer signifies the sell value. If valid, keep growing; else shrink/reset.
---
> [!info]- Why it works (the key insight)
> Continuing on why the brute force wasn't enough, we use sliding window to get the minimum (as of now) buy value, and keep growing from there, getting the max value with the current minimum. If we ever encounter a smaller buy value; reset and make it the current minimum, our left, and repeat.

## 6. Code
```rust
impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        // gameplan is; if valid, keep growing. else; shrink.
        let mut l = 0usize;
        let mut r = 0usize;
        let mut ans = 0i32;
        while r < prices.len() {
            let res = prices[r] - prices[l];
            if res < 0 {
                l = r; // we can reset here instead of l += 1
            } else {
                ans = if ans > res {ans} else {res};
                r += 1;
            }
        }
        ans
    }
}
```

## 7. Mistakes I actually made
- Minor mistake; but you should've used `l = r` on the shrink instead of `l += 1` because you already know it will break the loop in `l = r`.

## 8. Edge cases to always check for this pattern
- [ ] `l = r` (minimum window size 0 or 1)

## 9. Related problems
- 

---

### Flashcards