---
tags:
number: 981
title: Time Based Key-Value Store
url: https://leetcode.com/problems/time-based-key-value-store/
difficulty: Medium
pattern: Binary Search
status: solved
first-try: true
date-first-attempt: 2026-07-26
sr-due:
sr-interval: 1
sr-ease: 250
last-reviewed: 2026-07-27
---
## 1. Problem (in my own words)
Design a key-value store that also stores the timestamp. If a get command is invoked with the key `k` and timestamp `ts`, you need to return the most recent value (`t` <= `ts`).

## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                                                                                                   | Implication for approach                 |
| ------------------------------------------------------------------------------------------------------------ | ---------------------------------------- |
| `1 <= key.length, value.length <= 100`<br>`key` and `value` consist of lowercase English letters and digits. | not that important... (use string)       |
| `1 <= timestamp <= 10^7`                                                                                     | i32                                      |
| At most `2 * 10^5` calls will be made to `set` and `get`.                                                    | Up to $O(n \cdot log n)$ time complexity |
| All the timestamps `timestamp` of `set` are strictly increasing.                                             |                                          |

## 3. Recognition trigger
It's the same as binary search on answer, you need to search on a space that becomes `[1,1,1,0,0,0,0,0,...]`. 

## 4. Brute force

> [!info]- Idea
> Use a hash map to save the value and timestamp for the key. Browse through the value and timestamps of the given key and return the most recent.
---
>[!info]- Complexity 
>time $O(m)$ / space $O(n \cdot m)$
>`m` is the number of values a key can have; `n` is the number of keys that gets stored.
---
> [!warning]- Why it's not enough?
> It should be enough... but not optimized enough!

## 5. Optimal approach

> [!info]- Complexity 
>time $O(log m)$ / space $O(n \cdot m)$
---
> [!info]- Idea
> Use binary search on answer. Make the condition that the timestamp stored has to be less than the target timestamp.
---
> [!info]- Why it works (the key insight)
> Because of the 4th constraint, really.

## 6. Code
```python
# language: python

class TimeMap:
    def __init__(self):
        self.hmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.hmap: 
            self.hmap[key].append((timestamp, value))
        else:
            self.hmap[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.hmap:
            return ""
        kv = self.hmap[key]
        l = 0
        r = len(kv) - 1
        if timestamp < kv[0][0]:
            return ""
        while l < r:
            m = (l + r + 1) // 2
            if kv[m][0] <= timestamp:
                l = m
            else:
                r = m - 1

        return kv[l][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```

## 7. Mistakes I actually made
- Not knowing when to use `l <= r`, or `l < r`. Check [[binary search]] for the details.
- 

## 8. Edge cases to always check for this pattern
- [x] when no key is found

## 9. Related problems
- 

---