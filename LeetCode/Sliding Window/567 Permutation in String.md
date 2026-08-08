---
tags:
number: 567
title: Permutation in String
url: https://leetcode.com/problems/permutation-in-string/
difficulty: Medium
pattern: Sliding Window
status: solved
first-try: true
date-first-attempt: 2026-08-07
---
## 1. Problem (in my own words)
Given two strings `s1` and `s2`, find out if `s2` contains a permutation/anagram of itself inside `s1`. If so, return `true`. Else, return `false`.

## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                                          | Implication for approach    |
| --------------------------------------------------- | --------------------------- |
| `1 <= s1.length, s2.length <= 10^4`                 | Up to $O(n * m)$ complexity |
| `s1` and `s2` consist of lowercase English letters. | Predefined freq array       |

## 3. Recognition trigger
Again with the contiguous subrange, and you can only progress linearly.

## 4. Brute force

> [!info]- Idea
> Compare every substring of `s2` with `s1`. Check if they're anagrams.
---
>[!info]- Complexity 
>time $O(n^2 * m)$ / space $O(1)$
---
> [!warning]- Why it's not enough?
> Because you don't really need to compare every substring. Compare the ones with the same length as `s1`. Plus, you've already learned [[242 Valid Anagram|how to effectively check if two strings are anagrams]].

## 5. Optimal approach

> [!info]- Complexity 
>time $O(n \cdot m)$ / space $O(1)$
---
> [!info]- Idea
> What he said (up there)
---
> [!info]- Why it works (the key insight)
> Because.

## 6. Code
```rust
impl Solution {
    pub fn check_eq_slice(s1: &[i32; 26], s2: &[i32; 26]) -> bool {
        // println!("freq1: {:?}", s1);
        // println!("freqw: {:?}", s2);
        for i in 0..26 {
            if s1[i] != s2[i] {
                return false;
            }
        }
        true
    }

    pub fn check_inclusion(s1: String, s2: String) -> bool {
        let mut freq1 = [0i32;26];
        let mut freq_w = [0i32;26];
        let bytes1 = s1.into_bytes();
        let bytes2 = s2.into_bytes();
        let len = bytes1.len();
        let len2 = bytes2.len();

        if len > len2 {
            return false;
        }

        for idx in 0..len {
            freq1[(bytes1[idx] - b'a') as usize] += 1;
            freq_w[(bytes2[idx] - b'a') as usize] += 1;
        }
        
        for idx in 0..(bytes2.len() - len) {
            if Solution::check_eq_slice(&freq1, &freq_w) {
                return true;
            } else {
                freq_w[(bytes2[idx] - b'a') as usize] -= 1;
                freq_w[(bytes2[idx+len] - b'a') as usize] += 1;
            }
        }
        Solution::check_eq_slice(&freq1, &freq_w)
    }
}
```

## 7. Mistakes I actually made
- Off by one, forgot to do a final check.

## 8. Edge cases to always check for this pattern

## 9. Related problems
- [[242 Valid Anagram]]

---

### Flashcards

#flashcards/misclassified/{{pattern}} 
On 567 Permutation in String, I first reached for =={{wrong pattern}}==, but =={{the specific constraint/phrasing that ruled it out}}== should have pointed me to =={{correct pattern}}== instead.