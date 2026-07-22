---
tags:
  - stack
  - array
  - "#math"
number: 150
title: Evaluate Reverse Polish Notation
url: https://leetcode.com/problems/evaluate-reverse-polish-notation
difficulty: Medium
pattern: Stack
status: solved
first-try: true
date-first-attempt:
sr-due:
sr-interval: 1
sr-ease: 250
last-reviewed:
---
## 1. Problem (in my own words)
Given an array of strings (tokens) that describes an expression using the postfix notation, return the result of the expression.
The type of strings entered include:
- Numbers (`"0", "10", "109", ...`)
- Operator (`"*", "/", "+", "-"`)
## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                                                                                                                                                    | Implication for approach       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| `1 <= tokens.length <= 10^4`                                                                                                                                  | Up to $O(n^2)$ time complexity |
| No division by zero.                                                                                                                                          | Great. No need to handle this  |
| - Number inputs will be integers in the range `[-200, 200]`<br>- The answer and all the intermediate calculations can be represented in a **32-bit** integer. | int32 is enough                |

## 3. Recognition trigger
The most basic expression is `num, num, operator`. Operator needs the top two numbers. Gee I wonder what's

## 4. Brute force

> [!info]- Idea
> {{your idea here}}
---
>[!info]- Complexity 
>time $O({{your complexity here}})$ / space $O({{your complexity here}})$
---
> [!warning]- Why it's not enough?
> {{why?}}

## 5. Optimal approach

> [!info]- Complexity 
>time $O({{your complexity here}})$ / space $O({{your complexity here}})$
---
> [!info]- Idea
> {{your idea here}}
---
> [!info]- Why it works (the key insight)
> {{your insight here}}

## 6. Code
```python
# language: 

```

## 7. Mistakes I actually made
<!-- Be specific — "off by one in the while condition," not "careless." Vague entries don't help future-you. -->
- 
- 

## 8. Edge cases to always check for this pattern
- [ ] 
- [ ] 

## 9. Related problems
<!-- Link other notes: [[Two Sum]] -->
- 

---

### Flashcards

#flashcards/misclassified/{{pattern}} 
On 150 Evaluate Reverse Polish Notation, I first reached for =={{wrong pattern}}==, but =={{the specific constraint/phrasing that ruled it out}}== should have pointed me to =={{correct pattern}}== instead.