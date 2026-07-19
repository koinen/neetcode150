---
tags:
  - heap
title: Heaps
---
## What is it?
A data structure (array variant, like [[stack]] or [[queue]], etc.) that **guarantees the first element is the smallest/largest**, depends if your heap is a min-heap or a max-heap respectively. It doesn't do a full sorting, just putting the smallest/largest element in the front.

## Core ops + complexity

| **Core ops**       | **Complexity** |
| ------------------ | -------------- |
| push               | $O(log n)$     |
| pop min/max        | $O(log n)$     |
| peek               | $O(1)$         |
| heapify from array | $O(n)$         |
## Example usage
### Python
```python
import heapq # must import this package

# Heapify
data = [5, 1, 3, 7, 8] # uses a list as a base 
heapq.heapify(data) # Convert it into a min-heap in-place, 
# results in [1, 5, 7, 8, 3]

# Push
new_elmt = 4
heapq.heappush(data, new_elmt) # [1, 5, 2, 7, 8, 3, 4]
new_smallest_elmt = 0
heapq.heappush(data, new_smallest_elmt) # [0, 5, 1, 7, 8, 4, 3]

# Pop (min, since it's a min-heap by default)
popped_elmt = heapq.heappop(data) # 0, but it also makes sure the first element is still the smallest. hence, O(log n) complexity instead of O(n) or O(1)

# Peek
smallest = data[0] # since it's still a list.
```
## When you reach for it
- "k-th largest/smallest" without needing full sort
- streaming/online problems where you need running min/max
- merge k sorted lists/arrays
## Gotchas
- Python's `heapq` is min-heap only; negate values for max-heap
- `heapify` != repeated `push`, know which one your language gives you by default

---
## Confusable with
- [[Sorting]] when k is close to n; heap loses its advantage, just sort