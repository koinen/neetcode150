---
tags:
  - "#hashtable"
  - "#string"
  - "#sliding-window"
number: 3
title: Longest Substring Without Repeating Characters
url: https://leetcode.com/problems/longest-substring-without-repeating-characters
difficulty: Medium
pattern: Sliding Window
status: solved
first-try: true
date-first-attempt: 2026-08-06
---
## 1. Problem (in my own words)
Given a string `s`, find the longest substring without repeating characters.

For example:
`ccbbcc`, the longest substring would be `cb`.

## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint              | Implication for approach                 |
| ----------------------- | ---------------------------------------- |
| `0 <= s.length <= 10^5` | Up to $O(n \cdot log n)$ time complexity |

## 3. Recognition trigger
- It's a substring --> contiguous array range
- You need to keep track of what's going on inside the range; and need to grow/shrink accordingly.
- It grows linearly (move left/right one-by-one)

## 4. Brute force

> [!info]- Idea
> Iterate through every index (for the start), and find the longest substring from there.
---
>[!info]- Complexity 
>time $O(n^2)$ / space $O(1)$
---
> [!warning]- Why it's not enough?
> Because you're throwing away the information for the stored characters if you move to the next one; you're essentially repeating the work there.

## 5. Optimal approach

> [!info]- Complexity 
>time $O(n)$ / space $O(1)$
---
> [!info]- Idea
> Use sliding window, with some memory to keep track of what's happening inside the window. If you ever encounter the same character that exists in your window, cut the last occurrence, shifting your left pointer to the `last_occ + 1`.
---
> [!info]- Why it works (the key insight)
> It works because you're not repeating any work. Safely throwing out unusable part of the substring.

## 6. Code
```rust
use std::collections::HashMap;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        // gameplan: if valid, keep growing; else, shrink/reset.
        let mut last = [-1i32;256]; // this is an optimization on my part to get a faster time; ideally we use hashmap here.
        let mut l = 0i32;
        let mut ans = 0i32;
        for (i, c) in s.into_bytes().into_iter().enumerate() {
            let idx = c as usize;
            if (last[idx] >= l as i32) { // if last_idx is less than l, it means it's not even part of the current window, so skip.
                l = last[idx] + 1; // shift left to last_occ + 1
            }
            last[idx] = i as i32;
            ans = ans.max(i as i32 - l + 1);
        }
        ans
    }
}
```

## 7. Mistakes I actually made

## 8. Edge cases to always check for this pattern

## 9. Related problems

---

### Flashcards