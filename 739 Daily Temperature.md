---
tags:
  - "#stack"
  - "#staff"
  - "#array"
  - "#monotonic-stack"
number: 739
title: Daily Temperature
url: https://leetcode.com/problems/daily-temperatures/
difficulty: Medium
pattern: Stack
status: solved
first-try: true
date-first-attempt: 2026-07-23
sr-due:
sr-interval: 1
sr-ease: 250
last-reviewed: 2026-07-23
---
## 1. Problem (in my own words)
Given an array of integers `temperatures` that describes the temperatures of sequential days, return an array `answer` such that `answer[i]` is the number of days to get a warmer temperature than the `i-th` day (`temperatures[i]`). If there are no future days where it's warmer, keep `answer[i]` as `0`.

Example:
`Input: temperatures = [73,74,75,71,69,72,76,73]`
`Output: [1,1,4,2,1,1,0,0]`

## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                         | Implication for approach                |
| ---------------------------------- | --------------------------------------- |
| `1 <= temperatures.length <= 10^5` | Up to $O(n \cdot logn)$ time complexity |
| `30 <= temperatures[i] <= 100`     | int32                                   |

## 3. Recognition trigger
I need the information of the most recent larger value up to now. 

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
On 739 Daily Temperature, I first reached for =={{wrong pattern}}==, but =={{the specific constraint/phrasing that ruled it out}}== should have pointed me to =={{correct pattern}}== instead.