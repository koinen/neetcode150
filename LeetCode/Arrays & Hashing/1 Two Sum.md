---
tags:
  - "#hashtable"
  - array
number: 1
title: Two Sum
url: https://leetcode.com/problems/two-sum
difficulty: Easy
pattern: Arrays & Hashing
status: Done
date-first-attempt: 2021-11-03
sr-due:
sr-interval: 1
sr-ease: 250
last-reviewed: 2026-07-17
---
## 1. Problem (in my own words)
In an array of numbers, return the **two** indices of the elements where they sum to `target`.
## 2. Constraints & what they imply
<!-- e.g. n ≤ 10^5 → need O(n log n) or better. n ≤ 20 → bitmask/brute force is fine. -->
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                   | Implication for approach                      |
| ---------------------------- | --------------------------------------------- |
| `2 <= nums.length <= 10^4`   | up to $O(n^2)$ time complexity                |
| `-10^9 <= nums[i] <= 10^9`   | int32 is enough.                              |
| `-10^9 <= target <= 10^9`    | int32 is enough.                              |
| Exactly one solution exists. | we don't need to handle no solution edge case |

## 3. Recognition trigger
<!-- The single most important field. What SHOULD have told you the pattern, before you solved it?
This is what you're actually training — pattern recall, not the solution itself. -->
USE HASHMAP!!!
## 4. Brute force

>[!info]- Complexity 
>time $O(n^2)$ / space $O(1)$
---
> [!info]- Idea
> Loop through every element, and loop again to find the matching element that sums to `target`.
---
> [!warning]- Why it's not enough? 
> It is enough. XD

## 5. Optimal approach

> [!info]- Complexity 
> time $O(n)$ / space $O(n)$
---
> [!info]- Idea
> Use hashmap!!!
---
> [!info]- Why it works (the key insight)
> You can use the elements as a key, and just iterate through the array and check if `target-current` exists in the map.
## 6. Code
```python
# language: 
class Solution(object):
    def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		n = len(nums)
		hmap = {}
		for i in range(n):
			complement = target - nums[i]
			if complement in hmap:
				return [hmap[complement], i]
			if nums[i] not in hmap:
				hmap[nums[i]] = i

		return [0, 0]
```

## 7. Mistakes I actually made
<!-- Be specific — "off by one in the while condition," not "careless." Vague entries don't help future-you. -->
- I tried to do two passes, one for filling up the map, one for checking for solutions.
	This didn't work, because it introduces edge cases; if the target is the exact twice of the `nums[i]`, it will say it has been registered in the map, and it will return `[i, i]`.  

## 8. Edge cases to always check for this pattern
- None, if you use the one-pass.

## 9. Related problems
<!-- Link other notes: [[Two Sum]] -->
- None

---

#flashcard
What pattern does 1 Two Sum use, and what in the problem statement signals it? 
??
Arrays & Hashing — trigger: USE HASHMAP!!!

