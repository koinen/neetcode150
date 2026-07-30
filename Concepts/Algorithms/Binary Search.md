---
tags:
  - "#binary-search"
title: Binary Search
sr-due:
sr-ease:
sr-interval:
last-reviewed-at: 2026-07-27
---
## What is it?
Binary search is a search you can do on sorted arrays, given an exact target. The concept is simple. Take a look at the middle of the range; if it's smaller than your target, then the target must be in the right half, so go do search again in there, and vice versa.  

## Complexity (classic)
- Time: $O(log n)$
- Space: $O(1)$
## Example Usage
Go look at [[704 Binary Search]].
## Common Applications
- Binary search on answer; Typically the question will go find the minimum/maximum that satisfies X. In which case, you can transform the solution space to a monotonic `[f, f, f, ..., t, t, t, ...]`. and you can search the first true or the latest false by searching the boundary between `f` and `t`.
## Gotchas
- Know when to use `l <= r, l < r` and how to properly get the midpoints.
	- If you do an exact match search, you would do a `l <= r` boundary loop.
		- Shrink the array by using `l = m + 1`, and `r = m - 1`. 
		- Since it's an exact match search, you already know `m` won't ever be the answer.
	- If you're doing a boundary search, e.g. searching the first true/latest false on a monotonic `[f, f, f, ..., t, t, t, ...]` then you would need a `l < r` search, because `m` could be the answer; you can't safely throw it out. 
		- You would need to shrink it by using `l = m`, or `r = m` (keep the `m` if you know it could still be the answer; else use `l = m + 1` or `r = m - 1`. Typically it's one or the other; not both). 
		- If you're using `l = m`, make sure to get the `m` with `m = (l + r + 1) // 2`, or else you would end up in an infinite loop. 
		- `r = m` is safe with the usual `m = (l + r) // 2`. 

--- 

### Flashcards

#flashcards/concept
What is Binary Search and how does it work?
?
Binary search is a search you can do on sorted arrays, given an exact target. The concept is simple. Take a look at the middle of the range; if it's smaller than your target, then the target must be in the right half, so go do search again in there, and vice versa.  

#flashcards/concept
What's the typical time complexity of Binary Search?
?
$O(log n)$ time; $O(1)$ space

#flashcards/implementation/binary-search
When to use `l <= r` as opposed to `l < r`?
You would do `l <= r` if you're doing an exact search; `l < r` if you're doing a boundary search.

