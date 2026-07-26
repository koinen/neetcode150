---
tags:
number: 153
title: Find Minimum in Rotated Sorted Array
url: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
difficulty: Medium
pattern: Binary Search
status: solved
first-try: true
date-first-attempt: 2026-07-26
sr-due:
sr-interval: 1
sr-ease: 250
last-reviewed: 2026-07-26
---
## 1. Problem (in my own words)
Given an array of integers `arr`, in which it has been sorted in a non-descending order. However, it got rotated.

Rotated is when you translate the indices, for example:
Original: `[0, 1, 2, 3, 4, 5, 6, 7]`
Rotated: `[5, 6, 7, 0, 1, 2, 3, 4]`

## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                                                | Implication for approach                 |
| --------------------------------------------------------- | ---------------------------------------- |
| `1 <= n <= 5000`                                          | ~~$O(n^2 \cdot log n)$ time complexity~~ |
| All the integers of `nums` are **unique**.                | no need to handle duplicate cases        |
| You must write an algorithm that runs in `O(log n) time`. | b-b-b-binary search...?!                 |

## 3. Recognition trigger
$O(log n)$ time complexity. Sorted.

## 4. Brute force

> [!info]- Idea
> Scan through the array and find the minimum.
---
>[!info]- Complexity 
>time $O(n)$ / space $O(1)$
---
> [!warning]- Why it's not enough?
> You need to use the fact that it's sorted, even though it's rotated.

## 5. Optimal approach

> [!info]- Complexity 
>time $O(log n)$ / space $O(1)$
---
> [!info]- Idea
> Use binary search. However, you can't really apply it to the problem directly. Use the fact that it's sorted, and therefore if `arr[left] > arr[mid]`, the 'jump' from the rotation is in there; else, it's on the other half; or it could be that there's no rotation at all.
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
On 153 Find Minimum in Rotated Sorted Array, I first reached for =={{wrong pattern}}==, but =={{the specific constraint/phrasing that ruled it out}}== should have pointed me to =={{correct pattern}}== instead.