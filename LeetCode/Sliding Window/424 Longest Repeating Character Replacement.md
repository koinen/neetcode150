---
tags:
  - hashtable
  - string
  - sliding-window
number: 424
title: Longest Repeating Character Replacement
url: https://leetcode.com/problems/longest-repeating-character-replacement
difficulty: Medium
pattern: Sliding Window
status: solved
first-try:
date-first-attempt: 2026-08-07
---
## 1. Problem (in my own words)
Find the longest substring length that would result in a string of one repeated character if you can make at most `k` replacements to some letters in the substring. 

For example, to make this string a string of one repeated character; you would need to make 2 changes: `AAAAAABAAAB`, that is switching the B to an A.

## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                                      | Implication for approach                      |
| ----------------------------------------------- | --------------------------------------------- |
| `1 <= s.length <= 10^5`                         | Up to $O(n \cdot log n$) time complexity      |
| `s` consists of only uppercase English letters. | Predefined frequency map, no need for hashmap |

## 3. Recognition trigger
You need to keep track of what's going on inside a contiguous subrange, since it's a substring.
It also grows linearly, you can only check it one by one, since it isn't sorted in any way.

## 4. Brute force

> [!info]- Idea
> Iterate through every possible substring.
---
>[!info]- Complexity 
>time $O(n^3)$ / space $O(1)$
---
> [!warning]- Why it's not enough?
> Because... you're repeating work. Why not make it so that you keep start from size 0 and keep it growing until you find it invalid, and do something to keep it valid again.

## 5. Optimal approach

> [!info]- Complexity 
>time $O(n)$ / space $O(1)$
---
> [!info]- Idea
> Use sliding window. Keep track of the frequency inside the window. The validity check here is it's valid when `window_length - max_freq <= k`.  
---
> [!info]- Why it works (the key insight)
> It works because you don't really need to restart at the beginning. You can make use of the current one, keep sliding the window, since you need a contiguous range anyway.

## 6. Code
```rust
// language: rust

impl Solution {
    pub fn character_replacement(s: String, k: i32) -> i32 {
        // make a map that tracks frequency inside the window.
        // validity check: len - max(freq) <= k
        // for now, let's do shrink and grow one-by-one.
        let mut freq = [0i32;26];
        let mut ans = 0i32;
        let mut l = 0usize;
        let bytes = s.into_bytes();
        let mut max = 0;
        for (i, c) in bytes.iter().enumerate() {
            let idx = (c - b'A') as usize;
            freq[idx] += 1;
            max = max.max(freq[idx]);

            while l <= i && (i - l + 1) as i32 - max > k {
                let l_idx = (bytes[l] - b'A') as usize;
                freq[l_idx] -= 1;
                l += 1;
            }
            ans = ans.max((i - l + 1) as i32);
        }

        ans
    }
}
```

## 7. Mistakes I actually made
- Not a mistake, but an optimization miss
	- Use a predefined freq array instead of a hashmap.
	- Keep the stale maximum, no need to rederive it every time window gets changed. Since the answer wouldn't change when the maximum up until now gets exceeded. 

## 8. Edge cases to always check for this pattern

## 9. Related problems

---

### Flashcards