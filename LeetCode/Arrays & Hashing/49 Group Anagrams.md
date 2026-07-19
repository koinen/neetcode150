---
tags:
  - "#array"
  - "#hashtable"
  - "#string"
  - "#sorting"
number: 49
title: Group Anagrams
url: https://leetcode.com/problems/group-anagrams/
difficulty: Medium
pattern: Arrays & Hashing
status: solved
first-try: true
date-first-attempt: 2026-07-17
sr-due:
sr-interval: 1
sr-ease: 250
last-reviewed: 2026-07-17
---
## 1. Problem (in my own words)
Given an array of strings, group them based on if they are anagrams or not.
For example: `[ab, ba, bb]` would result in `[[ab, ba], [bb]]`, since `ab` and `ba` are anagrams.

## 2. Constraints & what they imply
<!-- e.g. n ≤ 10^5 → need O(n log n) or better. n ≤ 20 → bitmask/brute force is fine. -->
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                                                     | Implication for approach                                                                            |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| N:`1 <= strs.length <= 10^4`<br>M:`0 <= strs[i].length <= 100` | Effectively `10^6` if you loop through every character, therefore it can only go up to $O(N*log N)$ |
| `strs[i]` consists of lowercase English letters.               | doesn't change much, really                                                                         |
## 3. Recognition trigger
<!-- The single most important field. What SHOULD have told you the pattern, before you solved it? This is what you're actually training — pattern recall, not the solution itself. -->
You need to store information about what you just looped through, the information being occurrences for each character.
## 4. Brute force

> [!info]- Idea
> Use [[242 Valid Anagram]] as a function, and loop through the array of strings to check if the other string returns `true`. If `true`, add to the group; else, add a new group. 
---
>[!info]- Complexity 
>time $O(N^2 * M)$ / space $O(N)$
---
> [!warning]- Why it's not enough?
> Because it's way too much redundant work. Instead of scanning per string and comparing it to others, scan once and keep it in memory.

## 5. Optimal approach

> [!info]- Complexity 
>time $O(N * M)$ / space $O(N * M)$
---
> [!info]- Idea
> Use the same [[242 Valid Anagram]] character occurrence hashmap, and keep them inside another hashmap.
---
> [!info]- Why it works (the key insight)
> With the big hashmap, you can now check for an identical occurrences hashmap in $O(1)$, since we set it as a key.

> [!info]- Alternative idea
> Use sort and keep the sorted string as the key to the big hashmap.

## 6. Code
```python
# language: python
class Solution(object):
	def groupAnagrams(self, strs):
		"""
		:type strs: List[str]
		:rtype: List[List[str]]
		"""	
		big_map = {}
		for i in range(len(strs)):
			custom_hmap = [0 for k in range(26)]
			for j in strs[i]:
				custom_hmap[ord(j) - ord('a')] += 1 
			key = tuple(custom_hmap)
			if key not in big_map:
				big_map[key] = [i]
			else:
				big_map[key].append(i)
		
		ans = []
		for val in big_map.values():
			res = []
			for i in val:
				res.append(strs[i])
			ans.append(res)
			
		return ans
```

## 7. Mistakes I actually made
<!-- Be specific — "off by one in the while condition," not "careless." Vague entries don't help future-you. -->
- You can't keep a hashmap as a key (in python, at least. I don't know about other languages).
	- Well, make your own custom DS that can store that information. I will use an array sized 26, since it all consists of [[49 Group Anagrams#2. Constraints & what they imply|lowercase English letters]]. Use the index as the key for which alphabet, ex. index 0 means a, index 1 means b, and so on. 
	- Apparently lists aren't hashable as well. Solution I found was to wrap it inside a tuple 
		`key = tuple(list)`

## 8. Edge cases to always check for this pattern
- [x] None

## 9. Related problems
<!-- Link other notes: [[Two Sum]] -->
- [[242 Valid Anagram]]

---

#flashcards
What pattern does 49 Group Anagrams use, and what in the problem statement signals it? 
??
{{pattern}} — trigger: <fill in from section 3>
