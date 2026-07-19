---
tags:
  - sorting
title: Sorting
---
## Core ops + complexity
Just use your language's provided sorting algorithm, for standard sorts ascending or descending. Typically will always end up in $O(n \cdot log n)$ in time complexity

| Core ops | Complexity          |
| -------- | ------------------- |
| Sort     | $O (n \cdot log n)$ |
## Example Usage
- **Python**
```python
"""
there exists 2 methods to sort in python. one is to use .sort() on a list, and one is to use sorted(). the former mutates the list, whereas the latter returns the sorted list, leaving the original untouched.
""" 

"""
the param key takes in a function that's used as the comparator between two elements. common keys include:
key=lambda x: x[1] # usually used for sorting dictionary by value
key=lambda x: len(x) # usually used for sorting string by length
"""

"""
the param reversed takes in a boolean, if reversed you get the reversed sorted list. pretty self-explanatory.
"""

arr = [3, 2, 5, 7, 1, 4, 6]
arr.sort() # [1, 2, 3, 4, 5, 6, 7]
arr.sort(reverse=True) # [7, 6, 5, 4, 3, 2, 1]

arr = [3, 2, 5, 7, 1, 4, 6]

sorted_arr = sorted(arr) # [1, 2, 3, 4, 5, 6, 7]
sorted_arr = sorted(arr, reverse=True) # [7, 6, 5, 4, 3, 2, 1]
# arr stays as [3, 2, 5, 7, 1, 4, 6]
```
## When you reach for it
- When the problems don't ask for the indices, since you would need to track it if you sort.
- If you need patterns like [[Binary Search]] or [[Two Pointers]], but the array hasn't been sorted yet.
- If you need to process elements in a certain order to make your [[Greedy Algorithm]] work.
- If you need adjacency/grouping by value, not by position.
- When you're checking frequency/rank rather than raw value.

## Anti-signal (When you **SHOULDN'T** reach for it)
- If you need original indices in the output, as mentioned in the first point above
- If a linear-time solution exists, since even the best sort will always perform in $O(n \cdot log n)$ (except if there are certain conditions that have already been met; unique to the sorting algorithm)
## Confusable with
- [[Heaps]], if you need only a small part that's sorted instead of the whole array.

#flashcards 
What is Sorting and how does it work?
??
Sorting is ordering your array and make it sorted in order. 

#flashcards 
What's the typical time complexity of Sorting?
??
It's $O(n \cdot log n)$