---
tags:
  - "#two-pointers"
  - "#string"
number: 125
title: Valid Palindrome
url: https://leetcode.com/problems/valid-palindrome/
difficulty: Easy
pattern: Two Pointers
status: solved
first-try: true
date-first-attempt: 2026-07-20
sr-due:
sr-interval: 1
sr-ease: 250
last-reviewed: 2026-07-20
---
## 1. Problem (in my own words)
Check if a string is a palindrome or not after removing all the non-alphanumeric characters and cast all to lowercase.

What's a palindrome? it's when a string is spelt the same backwards, like racecar and such.
## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                                       | Implication for approach |
| ------------------------------------------------ | ------------------------ |
| `1 <= s.length <= 2 * 10^5`                      |                          |
| `s` consists only of printable ASCII characters. |                          |

## 3. Recognition trigger
Palindrome, you need to compare left and right at the same time, and move both pointers to the next element.

## 4. Brute force

> [!info]- Idea
> Compare the reversed copy character-by-character.
---
>[!info]- Complexity 
>time $O(n)$ / space $O(n)$
---
> [!warning]- Why it's not enough?
> It is enough, but a bit redundant for the extra space.

## 5. Optimal approach

> [!info]- Complexity 
>time $O(n)$ / space $O(1)$
---
> [!info]- Idea
> Use two pointers, one starting from the leftmost, the other starting from the rightmost.
---
> [!info]- Why it works (the key insight)
> You compare, move the pointers if they are equal, if they aren't, well return `False` instantly. Also, you can move them independent from each other if you encounter a non-alphanumeric character. It doesn't depend to a single variable, such that the pointers are `k` and `len-1-k`.

## 6. Code
```python
# language: python
class Solution:
	def isAlphaNumeric(self, c):
		a = ord(s[l])
            if ((a >= 48 and a <= 57) or (a >= 65 and a <= 90) or (a >= 97 and a <= 122)):
            return True
        return False
	
    def isPalindrome(self, s: str) -> bool:        
        l = 0
        r = len(s) - 1
        s = s.lower()
        while r >= l:
            if not self.isAplhaNumeric(s[l])
                l += 1
                continue
                
            if not self.isAlphaNumeric(s[r])
                r -= 1
                continue
            
            if (s[l] != s[r]):
                return False
            
            l += 1
            r -= 1
        
        return True
```

## 7. Mistakes I actually made
- forgot to use `.lower()`

## 8. Edge cases to always check for this pattern
- [x] None, two pointers covers all (at least in this problem)

## 9. Related problems

---

### Flashcards