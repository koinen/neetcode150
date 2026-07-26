---
tags:
  - hashtable
title: Hash Map
---
## What is it?


## Core ops + complexity

| Core ops            | Complexity                        |
| ------------------- | --------------------------------- |
| set                 | $O(1)$ average; $O(n)$ worst case |
| get                 | $O(1)$ average; $O(n)$ worst case |
| delete              | $O(1)$ average; $O(n)$ worst case |
| check if key exists | $O(1)$ average; $O(n)$ worst case |
| size                | $O(1)$                            |
## Example Usage
- **Python**
```python
# we can use python's dictionary. 

# init empty
hmap = {}

# init with initial elements
hmap = {'key1': 'val1', 'key2': 'val2'}

# set
key, value = 0, 1
hmap[key] = value

# get
print(hmap[key]) # will return error if key doesn't exist
print(hmap.get(key)) # safe get

# delete
del d[key]
value = d.pop(key) # both are unsafe, but you can use d.pop(key, fallback) to make it safe.

# check if key exists
if key in hmap:
	print("key is in hmap!")
```
## When you reach for it
- When you need to assign value to a certain key (duh). Typically used in frequency (for now at least).

## Confusable with
- [[Hash Set]]. don't use hashmap when you only assign true to a key; just use hashset at that point; more idiomatic.  

--- 
### Flashcards

#flashcards/concept
What is Hash Map and how does it work?
?
{{answer here}}
<!--SR:!2026-07-28,4,270-->

#flashcards/concept
What's the typical time complexity of Hash Map?
?
{{answer here}}
<!--SR:!2026-07-28,4,270-->

#flashcards/pattern
Hash Map applies when =={{condition A}}==, distinguishing it from {{competing pattern}}, which applies when =={{condition B}}==. The signal in problem statements is usually =={{phrasing/constraint that tips it off}}==.
<!--SR:!2026-07-28,4,270!2026-07-28,4,270!2026-07-28,4,270-->

#flashcards/implementation/{{pattern}}
{{Specific mechanical question — e.g. "In binary search, when should you use lo < hi vs lo <= hi?"}}
?
{{Answer, stated as a rule you can apply, not tied to one problem}}
<!--SR:!2026-07-28,4,270-->