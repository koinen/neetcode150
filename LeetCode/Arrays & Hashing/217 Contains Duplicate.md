---
tags:
  - "#array"
  - "#hashtable"
  - "#sorting"
number: 217
title: Contains Duplicate
url: https://leetcode.com/problems/contains-duplicate
difficulty: Easy
pattern: Arrays & Hashing
status: solved
first-try: true
date-first-attempt: 2026-07-16
sr-due:
sr-interval: 1
sr-ease: 250
last-reviewed: 2026-07-17
---
## 1. Problem (in my own words)
<!-- Rewrite the problem without looking at the original. If you can't, you don't understand it yet. -->
Return true if you found a duplicate in an array of numbers, else return false.

## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                 | Implication for approach               |
| -------------------------- | -------------------------------------- |
| `1 <= nums.length <= 10^5` | $O(n)$, a single loop should be enough |
| `-10^9 <= nums[i] <= 10^9` | int32 is enough                        |

## 3. Recognition trigger
<!-- The single most important field. What SHOULD have told you the pattern, before you solved it? This is what you're actually training — pattern recall, not the solution itself. -->
It's an array where you need to loop through elements and remember some information about what you just looped through.

## 4. Brute force

>[!info]- Complexity 
>time $O(n^2)$ / space $O(1)$
---
> [!info]- Idea
> Loop through every element and check if another element exists
---
> [!warning]- Why it's not enough?
> because it's a $O(n^2)$ in time complexity.

## 5. Optimal approach

> [!info]- Complexity 
> time $O(n)$ / space $O(n)$
---
> [!info]- Idea
> Loop through the elements but use a hashmap to save previous elements, and set them as the key.
---
> [!info]- Why it works (the key insight)
> Because using the numbers as keys in the hashmap effectively keeps them in your memory if you've found them or not, since access is also effectively $O(1)$.

## 6. Code
```python
# language: python
class Solution(object):
	def containsDuplicate(self, nums) -> bool:
		# nums is a List[int]
		hmap = {}
		for i in nums:
			if i in hmap:
				return True
			hmap[i] = True
		
		return False

```

## 7. Mistakes I actually made
<!-- Be specific — "off by one in the while condition," not "careless." Vague entries don't help future-you. -->
- NONE

## 8. Edge cases to always check for this pattern
- [x] Nothing

## 9. Related problems
- ...

---

#flashcards
What pattern does Easy - 217 Contains Duplicate use, and what in the problem statement signals it? 
??
Arrays & Hashing — trigger: Just use hashmap LOL