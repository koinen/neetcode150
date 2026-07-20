---
tags:
  - array
  - "#prefix-sum"
number: 238
title: Product of Array Except Self
url: https://leetcode.com/problems/product-of-array-except-self/
difficulty: Medium
pattern: Arrays & Hashing
status: solved-with-hints
first-try:
date-first-attempt: 2026-07-19
sr-due:
sr-interval: 1
sr-ease: 250
last-reviewed: 2026-07-19
---
## 1. Problem (in my own words)
<!-- Rewrite the problem without looking at the original. If you can't, you don't understand it yet. -->
Given an array of integers `nums`, return an array in which the elements are the product of all the other elements except itself. 

For example, in the input:
`[1, 2, 3, 4]`; the output would be `[24, 12, 8, 6]`.

## 2. Constraints & what they imply
<!-- e.g. n ≤ 10^5 → need O(n log n) or better. n ≤ 20 → bitmask/brute force is fine. -->
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                                                                                     | Implication for approach                                              |
| ---------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `2 <= nums.length <= 10^5`.                                                                    | -                                                                     |
| `-30 <= nums[i] <= 30`.                                                                        | -                                                                     |
| `O(n)` time complexity and no division operator.                                               | You can't use a multiply all and divide based on the current element. |
| The input is generated such that `answer[i]` is **guaranteed** to fit in a **32-bit** integer. | int32 is enough                                                       |
### Follow-up Constraint
| Constraint                     | Implication for approach                                                     |
| ------------------------------ | ---------------------------------------------------------------------------- |
| `O(1)` extra space complexity. | Try to use the information right then and there, no need to store in memory. |

## 3. Recognition trigger
<!-- The single most important field. What SHOULD have told you the pattern, before you solved it?
This is what you're actually training — pattern recall, not the solution itself. -->
It's an array... $O(n)$ complexity means you need to use just a simple linear scan.
## 4. Brute force

> [!info]- Idea
> Nested loop to populate each element of the output array.
---
>[!info]- Complexity 
>time $O(n^2)$ / space $O(1)$
---
> [!warning]- Why it's not enough?
> Because the problem wants $O(n)$, and there's a lot of redundant operations that can be stored in memory.

## 5. Optimal approach

> [!info]- Complexity 
>time $O(n)$ / space $O(1)$
---
> [!info]- Idea
> Use prefix/suffix, don't include the current element in it though.
---
> [!info]- Why it works (the key insight)
> Because it saves all the information that's necessary just by doing it once. 

## 6. Code

### Prefix-Suffix (Array)
```python
# language: python
class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		length = len(nums)
		
		prefix = [1 for i in range(length)]
		suffix = [1 for i in range(length)]
		
		for i in range(1, length):
			prefix[i] = prefix[i - 1] * nums[i - 1]
		
		for i in range(1, length):
			j = length - 1 - i
			suffix[j] = suffix[j + 1] * nums[j + 1]
		
		for i in range(length):
			prefix[i] *= suffix[i]
		
		return prefix 
```

### Prefix-Suffix (Single Element)
```python
# language: python
class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		length = len(nums)
		prefix = 1
		suffix = 1
		res = [1 for i in range(length)]
		for i in range(length):
			j = length - 1 - i
			res[j] = suffix
			suffix *= nums[j]

		for i in range(length):
			res[i] *= prefix
			prefix *= nums[i]
					
		return res
```
## 7. Mistakes I actually made
<!-- Be specific — "off by one in the while condition," not "careless." Vague entries don't help future-you. -->
- Off by one, wasn't sure where the range should begin and when it should end.

## 8. Edge cases to always check for this pattern
- [x] none

## 9. Related problems
<!-- Link other notes: [[Two Sum]] -->
- other prefix sum problems should go here...

---

#flashcards
What pattern does 238 Product of Array Except Self use, and what in the problem statement signals it? 
Given an array of integers `nums`, return an array in which the elements are the product of all the other elements except itself. 

For example, in the input:
`[1, 2, 3, 4]`; the output would be `[24, 12, 8, 6]`.
??
Arrays & Hashing — It's an array... $O(n)$ complexity means you need to use just a simple linear scan.

#flashcards
What's the key insight/tool that unlocks 238 Product of Array Except Self's complexity?
??
Prefix/Suffix Sum -- Because it saves all the information that's necessary just by doing it once. 