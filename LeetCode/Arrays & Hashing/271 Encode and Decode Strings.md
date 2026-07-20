---
tags:
  - array
  - string
  - "#design"
number: 271
title: Encode and Decode Strings
url: https://neetcode.io/problems/string-encode-and-decode/question
difficulty: Medium
pattern: Arrays & Hashing
status: solved
first-try:
date-first-attempt: 2026-07-18
sr-due:
sr-interval: 1
sr-ease: 250
last-reviewed:
---
## 1. Problem (in my own words)
Make an encoding and decoding algorithm for a list of strings. It has to be encoded to a single string, and be able to be decoded back to the original list of strings.

## 2. Constraints & what they imply
<!-- e.g. n ≤ 10^5 → need O(n log n) or better. n ≤ 20 → bitmask/brute force is fine. -->
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                                                                      | Implication for approach                                                                                        |
| ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `0 <= strs.length < 100`                                                        | I don't know what this implies. This doesn't really use that much logic or processing??                         |
| `0 <= strs[i].length < 200`                                                     | I don't know what this implies. This doesn't really use that much logic or processing??                         |
| `strs[i]` contains any possible characters out of `256` valid ASCII characters. | You can't keep the character as is, because you're not gonna have another character to be used as the separator |
- `m` is the sum of all the string lengths.
- `n` is `strs.length`.
### Follow-up constraint

| Constraint                                                                         | Implication for approach          |
| ---------------------------------------------------------------------------------- | --------------------------------- |
| Could you write a generalized algorithm to work on any possible set of characters? | You can't rely on ASCII encoding. |

## 3. Recognition trigger
<!-- The single most important field. What SHOULD have told you the pattern, before you solved it?
This is what you're actually training — pattern recall, not the solution itself. -->
I guess since you need to assign a symbol or something to the original character to make it reversible; therefore you need a hashtable (or some sort of alternative delimiter to tell the decoder to "stop, you've reached the end of this string.")
## 4. Brute force
This is not a complexity problem, so I personally think no "brute force" exists. I guess the hashtable would be the brute force.

> [!info]- Idea
> Loop through every character in the string; in the strings, and assign it to a number, save it in a hash map, so the decoder can use it. In the result string, just store the numbers, and make sure to separate them by a character (non-number), and use another character (non-number) as a delimiter.
---
>[!info]- Complexity 
>time $O(m)$ / space $O(k)$; $k$ being the amount of unique characters in all the strings. 
---
> [!warning]- Why it's not enough?
> It's enough, but unreliable; we don't have any control of `k`.

## 5. Optimal approach

> [!info]- Complexity 
>time $O(m+n)$ / space $O(m+n)$
---
> [!info]- Idea
> You can use the length of the string to let the decoder know when to stop and append the string.
---
> [!info]- Why it works (the key insight)
> You don't need to touch the string at all, just append it as is.

## 6. Code

### 1. Hashmap
```python
# language: python
class Solution:
	def __init__(self):
		self.hmap = {}
		self.k = 0
		self.separator = ' '
		self.delimiter = '_'
	
	def encode(self, strs: List[str]) -> str:
		res = ""
		for i in range(len(strs)):
			s = strs[i]
			for j in range(len(s)):
				num = self.k
				self.hmap[k] = s[j]
				res += f"{num}{self.separator}"
				self.k += 1
			res += self.delimiter
		print(res)
		return res
	
	def decode(self, s: str) -> List[str]:
		res = []
		i = 0
		while i < len(s):
			st = ""
			while i < len(s) and s[i] != self.delimiter:
				c = ""
				while s[i] != self.separator:
					c += s[i]
					i += 1
				st += self.hmap[int(c)]
				i += 1
			res.append(st)
			i += 1
		return res
```

### 2. Encoding the Length 
```python
# language: python
class Solution:	
	def __init__(self):
		self.separator = '#'
		
	def encode(self, strs: List[str]) -> str:
		res = ""
		for i in range(len(strs)):
			s = strs[i]
			res += f"{len(s)}{self.separator}{s}"
		print(res)
		return res
	
	def decode(self, s: str) -> List[str]:
		res = []
		i = 0
		while i < len(s):
			length = 0
			while s[i] != self.separator:
				length = length*10 + int(s[i])
				i += 1
			res.append(s[i+1:i+length+1]) # +1 to move to the next character (not the separator)
			i += length + 1
		return res
```
## 7. Mistakes I actually made
<!-- Be specific — "off by one in the while condition," not "careless." Vague entries don't help future-you. -->
- In **the optimal solution** (encoding the length), I incremented by `1` instead of `length + 1` at the end of the loop.

## 8. Edge cases to always check for this pattern
- [x] none

## 9. Related problems
<!-- Link other notes: [[Two Sum]] -->
- None

### Additional Notes
- this problem feels weird, as it doesn't really have that much thinking for how the algorithm should be, but rather a design problem; so technically there are bunch of solutions that can work, no "most optimal" one exists.

---

#flashcards
What pattern does 271 Encode and Decode Strings use, and what in the problem statement signals it? 
Make an encoding and decoding algorithm for a list of strings. It has to be encoded to a single string, and be able to be decoded back to the original list of strings.
??
Array & Hashing — trigger: I guess since you need to assign a symbol or something to the original character to make it reversible; therefore you need a hashtable (or some sort of alternative delimiter to tell the decoder to "stop, you've reached the end of this string.")

#flashcards
What's the key insight that unlocks 271 Encode and Decode Strings's complexity?
??
Encode in the string's length -- You don't need to touch the string at all, just append it as is. 