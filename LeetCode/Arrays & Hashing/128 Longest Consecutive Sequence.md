---
tags:
  - array
  - hashtable
  - "#union-find"
number: 128
title: Longest Consecutive Sequence
url: https://leetcode.com/problems/longest-consecutive-sequence
difficulty: Medium
pattern: Arrays & Hashing
status:
first-try:
date-first-attempt: 2026-07-20
sr-due:
sr-interval: 1
sr-ease: 250
last-reviewed: 2026-07-20
---
## 1. Problem (in my own words)
Given an unsorted array of integers, find the length of the longest consecutive sequence in the elements.

For example,
`input = [100, 4, 200, 1, 3, 2]` 
would output 4, because the longest consecutive sequence is `[1, 2, 3, 4]`.

## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                       | Implication for approach                                                         |
| -------------------------------- | -------------------------------------------------------------------------------- |
| `0 <= nums.length <= 10^5`       | ~~Up to $O(n \cdot logn)$ time complexity~~ invalidated by the third constraint. |
| `-10^9 <= nums[i] <= 10^9`       | int32 is enough                                                                  |
| Has to be $O(n)$ time complexity | Can't sort.                                                                      |

## 3. Recognition trigger
Can't sort. what else is there other than hash table amirite

## 4. Brute force

> [!info]- Idea
> Loop through the array, check for a bigger consecutive element by scanning through the array again for every element. Once found, try to scan again and find another. Keep track of the length while doing this, and maximum length as well. 
---
>[!info]- Complexity 
>time $O(n^2)$ / space $O(1)$
---
> [!warning]- Why it's not enough?
> Because we need $O(n)$ time complexity. Plus, there's a lot of redundant operations that can be optimized by using sort (start from the smallest) or hash table to check for existence.

## 5. Optimal approach

> [!info]- Complexity 
>time $O(n)$ / space $O(n)$
---
> [!info]- Idea
> Use hash table to keep track of existence....
---
> [!info]- Why it works (the key insight)
> Because you just need to check if key exists in the hash table; the key being the consecutive element.

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
On 128 Longest Consecutive Sequence, I first reached for =={{wrong pattern}}==, but =={{the specific constraint/phrasing that ruled it out}}== should have pointed me to =={{correct pattern}}== instead.