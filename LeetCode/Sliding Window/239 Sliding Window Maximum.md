---
tags:
number: 239
title: Sliding Window Maximum
url: https://leetcode.com/problems/sliding-window-maximum/
difficulty: Hard
pattern: Sliding Window
status: solved
first-try: true
date-first-attempt: 2026-08-08
---
## 1. Problem (in my own words)
Given an array `nums`, and an integer `k`, find the maximum of the `k`-sized windows of the array.

Example:
**Input:** nums = `[1,3,-1,-3,5,3,6,7]`, k = 3
**Output:** `[3,3,5,5,6,7]`
**Explanation:** 
```
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

## 2. Constraints & what they imply 
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                 | Implication for approach                 |
| -------------------------- | ---------------------------------------- |
| `1 <= nums.length <= 10^5` | Up to $O(n \cdot log n)$ time complexity |
| `1 <= k <= nums.length`    | `k` is always valid.                     |

## 3. Recognition trigger
Contiguous subrange (window). Linear growth.

## 4. Brute force

> [!info]- Idea
> Iterate through the windows and find the maximum.
---
>[!info]- Complexity 
>time $O(k \cdot (n - k))$ / space $O(1)$
---
> [!warning]- Why it's not enough?
> Again, because you're repeating work. You should be able to keep track previous windows, since it's only one number forgotten, one new number to keep track of. 

## 5. Optimal approach
### Heap (Suboptimal)
> [!info]- Complexity 
>time $O(n \cdot log n)$ / space $O(n)$
---
> [!info]- Idea
> Use sliding window and use a heap to keep track of the maximum of the window. But we need to make it so it describes the current state of the window. One way to work around this is keep the index of the element in the heap and compare it to the left index of the window.
---
> [!info]- Why it works (the key insight)
> It works because you perform a scan only once. 
### Deque (Optimal)
> [!info]- Complexity 
>time $O(n)$ / space $O(k)$
---
> [!info]- Idea
> Use sliding window, but keep a monotonic deque. The problem is surprisingly similar to [[155 Min Stack]], but instead of saving the minimum up to now; it's the maximum up to now, and the maximum can get stale (it's no longer inside the window). Therefore, we would also need to discard stale elements.
---
> [!info]- Why it works (the key insight)
> Because we always move to the right.
## 6. Code

### Heap
```rust
// language: rust

use std::collections::BinaryHeap;

impl Solution {
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut ans = vec![0;nums.len() - k as usize + 1];
        let mut l = 0;
        let mut heap = BinaryHeap::new();
        for i in 0..k-1 {
            heap.push((nums[i as usize], i));
        }
        for r in k-1..(nums.len() as i32) {
            heap.push((nums[r as usize], r));
            while let Some(&top) = heap.peek() {
                if top.1 >= l {
                    ans[l as usize] = top.0;
                    break;
                }
                heap.pop();
            }
            l += 1;
        }
        ans
    }
}
```

### Deque
```rust
// language: rust

use std::collections::BinaryHeap;
use std::collections::VecDeque;

impl Solution {
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut ans = vec![0;nums.len() - k as usize + 1];
        let mut l = 0;

        let mut dq = VecDeque::<(i32, i32)>::new();
        for i in 0..k-1 {
            while let Some(&top) = dq.back() {
                if nums[i as usize] < top.0 {
                    break;
                } 
                dq.pop_back();
            }
            dq.push_back((nums[i as usize], i));
        }
        
        for r in k-1..(nums.len() as i32) {
            while let Some(&top) = dq.back() {
                if nums[r as usize] < top.0 {
                    break;
                } 
                dq.pop_back();
            }
            dq.push_back((nums[r as usize], r));
            while let Some(&bot) = dq.front() {
                if bot.1 >= l {
                    ans[l as usize] = bot.0;
                    break;
                }
                dq.pop_front();
            }
            l += 1;
        }
        ans
    }
}
```
## 7. Mistakes I actually made
- I initially thought to just keep the maximum value, but that idea quickly falls apart because we can't find the next maximum. This leads me to the heap idea. But apparently there's a more optimized approach with deque. 

## 8. Edge cases to always check for this pattern
- [ ] 

## 9. Related problems
- 

---

### Flashcards