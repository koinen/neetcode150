---
tags:
  - "#stack"
title: Stack
---
## Core ops + complexity

| Core ops | Complexity |
| -------- | ---------- |
| Push     | $O(1)$     |
| Pop      | $O(1)$     |
| Peek     | $O(1)$     |
| IsEmpty  | $O(1)$     |
## Example Usage
- **Python**
```python
from collections import deque # python doesn't have a strictly "just stack" implementation

stack = deque() # you can also use list though, 
# stack = [] # it has the same ops signatures

# push
stack.append(1)

# peek
print(stack[-1])

# pop
top = stack.pop()

# isEmpty
if not stack:
	print("Stack is empty.")
```
## When you reach for it
- Typically, when you need some recent/latest information to proceed. 
- Usually, it's "the next greater/smaller element", in which case you can use a [[Monotonic Stack|monotonic stack]], where you get to merge elements based on conditions.
## Gotchas
- 

## Confusable with
- 

--- 

### Flashcards

#flashcards/concept
What is Stack and how does it work?
?
A LIFO data structure.
<!--SR:!2026-07-28,4,270-->

#flashcards/concept
What's the typical time complexity of Stack?
?
$O(1)$ for all operations (push, pop, peek, isEmpty)
<!--SR:!2026-07-28,4,270-->