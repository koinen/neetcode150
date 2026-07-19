---
tags:
  - array
  - hashtable
  - "#divide-and-conquer"
  - sorting
  - "#heap"
  - "#bucket-sort"
  - "#counting"
  - "#quickselect"
number: 347
title: Top K Frequent Elements
url: https://leetcode.com/problems/top-k-frequent-elements/
difficulty: Medium
pattern: Arrays & Hashing
status: Done
date-first-attempt: 2024-07-23
sr-due:
sr-interval: 1
sr-ease: 250
last-reviewed: 2026-07-17
---
## 1. Problem (in my own words)
Given an array of numbers, return an array containing the top-k most frequent elements. 
For example, given an array `[1, 2, 2, 1, 3, 2]`, their frequencies would be: 
```
{
	1: 2,
	2: 3,
	3: 1
}
```
if k = 1, return `[2]`, if k = 2, return `[2, 1]`, if k = 3, return `[2, 1, 3]`.
## 2. Constraints & what they imply
<!-- e.g. n ≤ 10^5 → need O(n log n) or better. n ≤ 20 → bitmask/brute force is fine. -->
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                                          | Implication for approach                                                                                                                                   |
| --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `1 <= nums.length <= 10^5`                          | $O(n \cdot logn)$ time complexity, sorting is allowed.                                                                                                     |
| `-10^4 <= nums[i] <= 10^4`                          | `int32` or even `int16` could do just fine.                                                                                                                |
| `k` is in the range <br>`[1, m*]`                   | No need to think for edge cases if `k > count` of unique elements.                                                                                         |
| It is **guaranteed** that the answer is **unique**. | No need to think for defined behavior for edge cases if a number has the same frequency as another, competing against the same spot if it exceeds top `k`. |
\*`m` is the number of unique elements in the array.
### Follow-up constraint

| Constraint                                              | Implication for approach                    |
| ------------------------------------------------------- | ------------------------------------------- |
| Has to be faster than $O(n \cdot logn)$ time complexity | No sorting allowed (at least based on `n`). |
## 3. Recognition trigger
Frequency almost always means hashmap. Top-k indicates it needs either **sorting** or using a **heap**.
## 4. Brute force

> [!info]- Idea
> Loop through every element of the array, and loop again to scan the count of the current element. Store the results in an array, as a tuple, with the frequency saved. Next, just loop through the results array and find the top-K frequency, and return the corresponding elements as an array.
---
>[!info]- Complexity 
>time $O(n^2)$ / space $O(n)$
---
> [!warning]- Why it's not enough?
> A lot of redundant operations; can be saved into memory to avoid recomputing the same thing

## 5. Optimal approach

### Minimum Heap

> [!info]- Complexity 
>time $O(m \cdot log n)$ / space $O(m)$
---
> [!info]- Idea
> 
---
> [!info]- Why it works (the key insight)
> {{your insight here}}
### Bucket Sort
## 6. Code
### 1. Standard Sort (Doesn't fulfill the follow-up constraint)
```python
# language: 
class Solution(object):
	def topKFrequent(self, nums, k):
		hmap = {}
		for i in nums:
			if i not in hmap:
				hmap[i] = 1
			else:
				hmap[i] += 1
		sorted_dict_desc = dict(sorted(hmap.items(), key=lambda item: item[1], reverse=True))
		
		return list(sorted_dict_desc.keys())[:k]
```

### 2. Minimum Heap
```python
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        hmap = {}
        for i in nums:
            if i not in hmap:
                hmap[i] = 1
            else:
                hmap[i] += 1
        
        my_heap = []
        for key, val in hmap.items():
            print(my_heap)
            heapq.heappush(my_heap, (val, key))
            if len(my_heap) > k:
                heapq.heappop(my_heap)

        print(my_heap)
        res = []
        for _, i in my_heap:
            res.append(i)
        
        return res
```

### 3. Bucket Sort
```python
class Solution(object):
    def topKFrequent(self, nums, k):
        hmap = {}
        for i in nums:
            if i not in hmap:
                hmap[i] = 1
            else:
                hmap[i] += 1
        
        buckets = [[] for i in range(len(nums)+1)]
        for key, val in hmap.items():
            buckets[val].append(key)
        
        res = []
        i = len(nums)
        while len(res) < k and i > 0:
            if buckets[i]:
                for j in buckets[i]:
                    if len(res) > k:
                        break
                    res.append(j)
            i -= 1

        return res
```
## 7. Mistakes I actually made
- I thought a heap was an automatically sorting array. [[Heaps#What is it?|Apparently not.]] 

## 8. Edge cases to always check for this pattern
- [x] None

## 9. Related problems
<!-- Link other notes: [[Two Sum]] -->
- 

---

#flashcard
What pattern does 347 Top K Frequent Elements use, and what in the problem statement signals it? 
??
{{pattern}} — trigger: <fill in from section 3>