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
### Suboptimal
> [!info]- Complexity 
>time $O(n \cdot log n)$ / space $O(n)$
---
> [!info]- Idea
> Use sliding window and use a heap to keep track of the maximum of the window. But we need to make it so it describes the current state of the window. One way to work around this is keep the index of the element in the heap and compare it to the left index of the window.
---
> [!info]- Why it works (the key insight)
> It works because 
### Optimal
> [!info]- Complexity 
>time $O(n)$ / space $O({{your complexity here}})$
---
> [!info]- Idea
> {{your idea here}}
---
> [!info]- Why it works (the key insight)
> {{your insight here}}
## 6. Code
```python
# language: 

```

## 7. Mistakes I actually made
<!-- Be specific — "off by one in the while condition," not "careless." Vague entries don't help future-you. -->
- 
- 

## 8. Edge cases to always check for this pattern
- [ ] 
- [ ] 

## 9. Related problems
<!-- Link other notes: [[Two Sum]] -->
- 

---

### Flashcards

#flashcards/misclassified/{{pattern}} 
On 239 Sliding Window Maximum, I first reached for =={{wrong pattern}}==, but =={{the specific constraint/phrasing that ruled it out}}== should have pointed me to =={{correct pattern}}== instead.