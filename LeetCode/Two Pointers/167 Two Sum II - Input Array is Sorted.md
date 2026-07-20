---
tags:
  - array
  - two-pointers
number: 167
title: Two Sum II - Input Array is Sorted
url: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
difficulty: Medium
pattern: Two Pointers
status:
first-try:
date-first-attempt: 2026-07-20
sr-due:
sr-interval: 1
sr-ease: 250
last-reviewed: 2026-07-20
---
## 1. Problem (in my own words)
Basically [[1 Two Sum]], but array is already sorted. Also, the **array is 1-indexed**, for whatever reason.

## 2. Constraints & what they imply
<!-- e.g. n ≤ 10^5 → need O(n log n) or better. n ≤ 20 → bitmask/brute force is fine. -->
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                                                     | Implication for approach                                       |
| -------------------------------------------------------------- | -------------------------------------------------------------- |
| `2 <= numbers.length <= 3 * 10^4`                              | Up to $O(n \cdot log n)$ time complexity; $O(n^2)$ is a no-no. |
| - `-1000 <= numbers[i] <= 1000`<br>- `-1000 <= target <= 1000` |                                                                |
| $O(1)$ extra space                                             | No hash tables.                                                |
| Only one solution exists                                       |                                                                |

## 3. Recognition trigger
<!-- The single most important field. What SHOULD have told you the pattern, before you solved it?
This is what you're actually training — pattern recall, not the solution itself. -->

## 4. Brute force

> [!info]- Idea
> {{your idea here}}
---
>[!info]- Complexity 
>time $O({{your complexity here}})$ / space $O({{your complexity here}})$
---
> [!warning]- Why it's not enough?
> {{why?}}

## 5. Optimal approach

> [!info]- Complexity 
>time $O({{your complexity here}})$ / space $O({{your complexity here}})$
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
On 167 Two Sum II - Input Array is Sorted, I first reached for =={{wrong pattern}}==, but =={{the specific constraint/phrasing that ruled it out}}== should have pointed me to =={{correct pattern}}== instead.