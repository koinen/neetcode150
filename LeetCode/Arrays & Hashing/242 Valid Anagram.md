---
tags:
  - "#hashtable"
  - "#string"
  - "#sorting"
number: 242
title: Valid Anagram
url: https://leetcode.com/problems/valid-anagram
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
Given an array of strings, group them based on if they are anagrams or not.

## 2. Constraints & what they imply
<!-- e.g. n ≤ 10^5 → need O(n log n) or better. n ≤ 20 → bitmask/brute force is fine. -->
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                                        | Implication for approach       |
| ------------------------------------------------- | ------------------------------ |
| `1 <= s.length, t.length <= 5 * 10^4`             | up to $O(s*t)$ time complexity |
| `s` and `t` consist of lowercase English letters. | ... doesn't change much.       |

## 3. Recognition trigger
<!-- The single most important field. What SHOULD have told you **the pattern**, before you solved it?
This is what you're actually training — pattern recall, not the solution itself. -->

## 4. Brute force

>[!info]- Complexity 
>time $O(s!)$ / space $O(1)$
---
> [!info]- Idea
> Find permutations of `s` until it equals `t`. If not found, they're not anagrams.
---
> [!warning]- Why it's not enough?
> because it's factorial....

## 5. Optimal approach

> [!info]- Complexity 
> time $O(s)$ / space $O(s)$
---
> [!info]- Idea
> Use hashmap!!!
---
> [!info]- Why it works (the key insight)
> This works because instead of rearranging, we can check for the count for each character. If they have the same count, they will be anagrams. Also if their length differs, it's an instant false.
## 6. Code
```python
# language: 
class Solution(object):
	def isAnagram(self, s: str, t: str) -> bool:
		if len(s) != len(t):
			return False
		hmap = {}
		for i in s:
			if i in hmap:
				hmap[i] += 1
			else:
				hmap[i] = 1
			
		for i in t:
			if i in hmap:
				hmap[i] -= 1
			else:
				return False
				
		for val in hmap.values():
			if val != 0:
				return False
		
		return True
				
```

## 7. Mistakes I actually made
<!-- Be specific — "off by one in the while condition," not "careless." Vague entries don't help future-you. -->
- None, only syntax problems 

## 8. Edge cases to always check for this pattern
- None

## 9. Related problems
<!-- Link other notes: [[Two Sum]] -->
- [[49 Group Anagrams]]

---
### Flashcards

#flashcards
What pattern does 242 Valid Anagram use, and what in the problem statement signals it? 
Given an array of strings, group them based on if they are anagrams or not.
?
Arrays & Hashing — trigger: USE HASHMAP!!!