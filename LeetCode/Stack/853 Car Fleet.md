---
tags:
  - stack
  - monotonic-stack
  - array
  - "#sorting"
number: 853
title: Car Fleet
url: https://leetcode.com/problems/car-fleet/
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
There are `n` cars, all travelling in the same direction to the mile `target`. You are given the starting position and speed of each car. A "fleet" is formed when a car catches up to another car. The fleet will have the speed of the slowest car. Cars can't overlap each other.
You are here to find out how many fleet will be formed when all the cars have reached `target`. 

`Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]`
`Output: 3`
## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint       | Implication for approach |
| ---------------- | ------------------------ |
| `1 <= n <= 10^5` | Up to $O(n \cdot log n)$ |

## 3. Recognition trigger
You need to merge with a bigger/smaller/some certain condition`*` element. (condition being slower, since the faster car would form a fleet and merge, effectively becoming the slower car)

## 4. Brute force

> [!info]- Idea
> Find out which elements can get merged, by scanning if there are any slower cars that are ahead of itself, and merge them, move to the next car.
---
>[!info]- Complexity 
>time $O(n^2)$ / space $O(1)$
---
> [!warning]- Why it's not enough?
> Because, we don't really need to scramble to find which cars are ahead of the current one; plus instead of sequentially checking each element one-by-one, we can make use our memory to save the mergeable cars.

## 5. Optimal approach

> [!info]- Complexity 
>time $O(n \cdot log n)$ / space $O(n)$
---
> [!info]- Idea
> Use a decreasing [[Monotonic Stack|monotonic stack]], with the time taken as the value. Since a car/fleet having a larger time means it's gonna be slower, and therefore any car faster **and behind** than it should get merged to it. 
---
> [!info]- Why it works (the key insight)
> Since a stack is LIFO, we get to use the top, which is the 'fastest current fleet' to compare and merge. 
## 6. Code
```python
# language: python
from collections import deque

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = [(position[i], (target - position[i])/speed[i]) for i in range(len(position))]

        combined.sort(key=lambda x: x[0])
        stack = deque()
        for _, time in combined:
            while stack and time >= stack[-1]:
                stack.pop()
            stack.append(time)
        
        return len(stack)
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
On 853 Car Fleet, I first reached for =={{wrong pattern}}==, but =={{the specific constraint/phrasing that ruled it out}}== should have pointed me to =={{correct pattern}}== instead.