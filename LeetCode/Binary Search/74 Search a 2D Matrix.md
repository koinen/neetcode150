---
tags:
  - "#array"
  - "#binary-search"
  - "#matrix"
number: 74
title: Search a 2D Matrix
url: https://leetcode.com/problems/search-a-2d-matrix
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
Do a search of an integer on a 2D matrix, which has been sorted in a non-descending order. Return `true` if found, else return `false`. 

## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                                                        | Implication for approach                                                         |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `1 <= m, n <= 100`                                                | ~~Up to $O((n\cdot m)^2)$ time complexity~~ invalidated by the third constraint. |
| `-10^4 <= matrix[i][j], target <= 10^4`                           | int32 is enough yadayada                                                         |
| You must write a solution in $O(log(m \cdot n))$ time complexity. | b-b-binary search...                                                             |

## 3. Recognition trigger
Sorted, $O(log (...))$ time complexity.

## 4. Brute force

> [!info]- Idea
> Scan through the array and just inspect the elements one by one.
---
>[!info]- Complexity 
>time $O(n\cdot m)$ / space $O(1)$
---
> [!warning]- Why it's not enough?
> Why don't you use the fact that it's sorted instead of inspecting it one-by-one, to skip some elements.

## 5. Optimal approach

> [!info]- Complexity 
>time $O(log(m\cdot n))$ / space $O(1)$
---
> [!info]- Idea
> "Flatten" the matrix to an array, and use binary search.
---
> [!info]- Why it works (the key insight)
> Because.

## 6. Code
```python
# language: python

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h = len(matrix)
        w = len(matrix[0])
        l = 0
        r = w*h - 1
        while l <= r:
            m = (l + r) // 2
            row = m // w
            col = m % w

            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False
```

## 7. Mistakes I actually made
- none

## 8. Edge cases to always check for this pattern
- [x] no

## 9. Related problems
- [[704 Binary Search]]

---

### Flashcards