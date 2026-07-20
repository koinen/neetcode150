---
tags:
  - array
  - hashtable
  - "#union-find"
number: 128
title: Longest Consecutive Sequence
url: https://leetcode.com/problems/longest-consecutive-sequence
difficulty: Medium
pattern: Arrays & Hashing
status: solved
first-try: true
date-first-attempt: 2026-07-20
sr-due:
sr-interval: 1
sr-ease: 250
last-reviewed: 2026-07-20
---
## 1. Problem (in my own words)
Given an unsorted array of integers, find the length of the longest consecutive sequence in the elements.

For example,
`input = [100, 4, 200, 1, 3, 2]` 
would output 4, because the longest consecutive sequence is `[1, 2, 3, 4]`.

## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                       | Implication for approach                                                         |
| -------------------------------- | -------------------------------------------------------------------------------- |
| `0 <= nums.length <= 10^5`       | ~~Up to $O(n \cdot logn)$ time complexity~~ invalidated by the third constraint. |
| `-10^9 <= nums[i] <= 10^9`       | int32 is enough                                                                  |
| Has to be $O(n)$ time complexity | Can't sort.                                                                      |

## 3. Recognition trigger
Can't sort. what else is there other than hash table amirite

## 4. Brute force

> [!info]- Idea
> Loop through the array, check for a bigger consecutive element by scanning through the array again for every element. Once found, try to scan again and find another. Keep track of the length while doing this, and maximum length as well. 
---
>[!info]- Complexity 
>time $O(n^2)$ / space $O(1)$
---
> [!warning]- Why it's not enough?
> Because we need $O(n)$ time complexity. Plus, there's a lot of redundant operations that can be optimized by using sort (start from the smallest) or hash table to check for existence.

## 5. Optimal approach

### DP
> [!info]- Complexity 
>time $O(n)$ / space $O(n)$
---
> [!info]- Idea
> Use a hashtable and DP, first; store the element and which index it is. second; store the length of the longest consecutive sequence from that element: `element, element + 1, ...` and loop through the array with that. if it's `elmt + 1` is filled, use it by `dp[elmt] = dp[elmt+1]`; else, fill it.
---
> [!info]- Why it is redundant.
> Because you're doing the counts for the partial sequence as well, when you could just skip through and start from the smallest. Also, all the hash table lookups stacks up.
### Hash Set
> [!info]- Complexity 
>time $O(n)$ / space $O(n)$
---
> [!info]- Idea
> Use hash set to keep track of existence
---
> [!info]- Why it works (the key insight)
> Because you just need to check if key exists in the hash table; the key being the next consecutive element. Also, important to do is start only from the lowest to prevent redundant work.

## 6. Code
### DP
```python
# language: 
class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		table = {}
		for i, val in enumerate(nums):
			table[val] = i
	
		dp = [-1 for i in range(len(nums))]
		ans = 0
	
		for val in table.keys():
			if dp[table[val]] != -1:
				continue
			k = 1
			
			while (val+k) in table and (dp[table[val+k]] == -1):
				k += 1
	
			if (val + k) not in table:
				dp[table[val+k-1]] = 1
			else:
				dp[table[val+k-1]] = dp[table[val+k]] + 1
				
			k -= 1
			while k > 0:
				dp[table[val+k-1]] = dp[table[val+k]] + 1
				k -= 1

			ans = max(dp[table[val+k]], ans)
	
		return ans
```
### Hash Set
```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0
        length = 0
        for i in num_set: # for some reason, iterating through nums resulted in TLE
            if i - 1 not in num_set:
                length = 1
                while (i + length) in num_set:
                    length += 1
                ans = max(ans, length)

        return ans
```
## 7. Mistakes I actually made
- Don't use raw `nums`, use the set instead in case it has high duplication.
- DP isn't always the best way to prevent redundant work, if you can truly go in one shot, DP just adds overhead.

> The actual signal to look for next time: when adjacency/recurrence is defined by _value relationships_ rather than _array position_, and there's no natural order to process elements in, that's a hash-set/hash-map membership problem, not DP. The $O(n)$ requirement is your confirmation — it's telling you "don't sort, don't do combinatorial subproblem buildup, just get $O(1)$ lookups and be smart about which elements you start counting from."

## 8. Edge cases to always check for this pattern
- [x] None

## 9. Related problems
<!-- Link other notes: [[Two Sum]] -->

---

### Flashcards

#flashcards/misclassified/arrays-and-hashing
On 128 Longest Consecutive Sequence, I first reached for Dynamic Programming, but ==The $O(n)$  time complexity requirement== should have pointed me to ==Hash-set== instead.