---
tags:
  - hashtable
title: Hash Set
---
## What is it?
It's the representation of the mathematical concept: set. It can store elements, in which all elements are unique, even if it gets inserted the same element twice or more. 

It's designed around one idea, which is for **fast membership testing**
## Core ops + complexity

| Core ops                     | Complexity                         |
| ---------------------------- | ---------------------------------- |
| add/insert                   | $O(1)$ average; $O(n)$ worst case. |
| contains (existence check)   | $O(1)$ average; $O(n)$ worst case  |
| remove                       | $O(1)$ average; $O(n)$ worst case  |
| size                         | $O(1)$                             |
| isEmpty                      | $O(1)$                             |
| clear (removes all elements) | $O(n)$                             |
| set-ify                      | $O(n)$                             |
## Example Usage
- **Python**
```python
# init empty
hset = set()

# init with initial elements
hset1 = {1, 2, 3, 4, 5, 6} # be careful! init with {} results in a dict instead of an empty set. empty set uses set() as a constructor.

# init from list (set-ify)
hset2 = set([1, 2, 3, 3, 4, 4])

# add/insert
hset.add(5)

# remove
hset.remove(5) # returns error if 5 is not in the set
hset.discard(4) # no error even if 4 is not in the set

# contains
if 5 in hset:
	print("5 exists in the set!")

# size
print(len(hset))

# clear 
hset.clear()
```
## When you reach for it
- You just need **fast membership testing**, no values assigned to the members.

--- 
### Flashcards

#flashcards/concept
What is Hash Set and how does it work?
?
It's the representation of the mathematical concept: set. It can store elements, in which all elements are unique, even if it gets inserted the same element twice or more. 
It's designed around one idea, which is for **fast membership testing**

#flashcards/concept

| Core ops                     | Complexity                             |
| ---------------------------- | -------------------------------------- |
| add/insert                   | ==$O(1)$ average; $O(n)$ worst case.== |
| contains (existence check)   | ==$O(1)$ average; $O(n)$ worst case==  |
| remove                       | ==$O(1)$ average; $O(n)$ worst case==  |
| size                         | $O(1)$                                 |
| isEmpty                      | $O(1)$                                 |
| clear (removes all elements) | $O(n)$                                 |
| set-ify                      | $O(n)$                                 |

#flashcards/pattern
Hash Set applies when ==you just need an existence check==, distinguishing it from Hash Map, which applies when ==where you need to assign some value to the element==. The signal in problem statements is usually ==unique elements, ==.

#flashcards/implementation/{{pattern}}
{{Specific mechanical question — e.g. "In binary search, when should you use lo < hi vs lo <= hi?"}}
?
{{Answer, stated as a rule you can apply, not tied to one problem}}