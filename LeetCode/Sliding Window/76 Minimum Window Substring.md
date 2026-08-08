---
tags:
number: 76
title: Minimum Window Substring
url: https://leetcode.com/problems/minimum-window-substring/
difficulty: Hard
pattern: Sliding Window
status: solved-with-hints
first-try:
date-first-attempt: 2026-08-08
---
## 1. Problem (in my own words)
Given two strings, `s` and `t`, find the minimum length substring of `s` that contains all the elements of `t`. 

## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                                                              | Implication for approach                 |
| ----------------------------------------------------------------------- | ---------------------------------------- |
| `1 <= m, n <= 10^5`. WLOG `m` and `n` is the length of both the strings | Up to $O(n \cdot log m)$ time complexity |
| `s` and `t` consist of uppercase and lowercase English letters.         | Predefined frequency map size            |

## 3. Recognition trigger
- Substring --> contiguous subrange. 
- unordered -> linear scan. 
- contains all elements -> frequency map

## 4. Brute force

> [!info]- Idea
> Inspect all possible `s` substrings, and compare it to `t` if it does contain all the elements or not.
---
>[!info]- Complexity 
>time $O(n^2 \cdot m)$ / space $O(1)$
---
> [!warning]- Why it's not enough?
> It ain't enough because you're repeating the work. Why bother inspecting the whole substring, when you can keep a substring and grow it one-by-one, inspect it if it is valid or not, and find the minimum from that

## 5. Optimal approach

> [!info]- Complexity 
>time $O(m + n)$ / space $O(1)$
---
> [!info]- Idea
> Sliding window, but instead of finding the maximum like the previous problems, here you need to grow until valid, and shrink while valid, find the minimum there.
---
> [!info]- Why it works (the key insight)
> It works because you don't really need to inspect the substrings one by one. By making it grow one-by-one you can already inspect what's going on inside the current substring in your memory and inspecting the changes is enough to determine whether it's valid or not. 

## 6. Code
```rust
impl Solution {
    pub fn min_window(s: String, t: String) -> String {
        // gameplan: grow until valid, shrink until invalid again.
        // validity check: freq map

        if t.len() > s.len() {
            return String::new();
        }

        let sbytes = s.as_bytes();
        let tbytes = t.as_bytes();

        let mut wfreq = [0i32;52];
        let mut tfreq = [0i32;52];

        let mut need = 0;
        for c in tbytes {
            let idx = if *c >= b'a' {
                (c - b'a') as usize + 26
            } else {
                (c - b'A') as usize
            };
            if tfreq[idx] == 0 {
                need += 1;  
            }
            tfreq[idx] += 1;
        }

        let mut l = 0;
        let mut have = 0;

        let (mut left, mut right) = (0, -1i32);
        for (i, c) in sbytes.iter().enumerate() {
            let idx = if *c >= b'a' {
                (*c - b'a') as usize + 26
            } else {
                (*c - b'A') as usize
            };    
            wfreq[idx] += 1;
            if tfreq[idx] == wfreq[idx] {
                have += 1;
            }
            while l <= i && have == need {
                if right == -1 || i - l < right as usize - left {
                    right = i as i32;
                    left = l;
                    // println!("left={:?}, right={:?}", left, right);
                }
                let l_idx = if sbytes[l] >= b'a' {
                    (sbytes[l] - b'a') as usize + 26
                } else {
                    (sbytes[l] - b'A') as usize
                };
                if wfreq[l_idx] == tfreq[l_idx] {
                    have -= 1;
                }
                wfreq[l_idx] -= 1;
                l += 1;
            }
        }
        if right == -1 {
            String::new()
        } else {
            String::from_utf8(sbytes[left..(right+1) as usize].to_vec()).unwrap()
        }
    }
}
```

## 7. Mistakes I actually made
- I initially thought the window should start as the whole string (entire opposite from the usual start from empty, grow while valid; shrink if not), but apparently you still start at empty and grow until valid, shrink while valid.

## 8. Edge cases to always check for this pattern
- [ ] No answer guaranteed, handle cases when input is definitely invalid or when no answer is found.

## 9. Related problems
- 

---

### Flashcards