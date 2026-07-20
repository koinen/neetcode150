---
tags:
  - array
  - hashtable
  - "#matrix"
number: 36
title: Valid Sudoku
url: https://leetcode.com/problems/valid-sudoku
difficulty: Medium
pattern: Arrays & Hashing
status: solved
first-try: true
date-first-attempt: 2026-07-20
sr-due:
sr-interval: 1
sr-ease: 250
last-reviewed: 2026-07-20
---
## 1. Problem (in my own words)
Given a `9x9`-sized sudoku board, check if it is a valid sudoku puzzle.

What is a valid sudoku puzzle?
- It is a partially filled sudoku board.
- The board will only be populated with values `1-9`, or `.` to indicate it isn't filled.
- No duplicates in the same row or column.
- No duplicates in each of the 9 sub-board (divide the column and row by 3).

**Valid != Solvable**
## 2. Constraints & what they imply
[[Constraint to Complexity Reference|See here for reference]]

| Constraint                               | Implication for approach |
| ---------------------------------------- | ------------------------ |
| `board.length == 9`                      |                          |
| `board[i].length == 9`                   |                          |
| `board[i][j]` is a digit `1-9` or `'.'`. |                          |

## 3. Recognition trigger
You need a fast lookup to check existence.

## 4. Brute force

> [!info]- Idea
> Scan through every row and column, check duplicate by looping through every element and loop through other elements and comparing it. Scan through every sub-board and do the same.
---
>[!info]- Complexity 
>time $O({{n^3}})$ / space $O({{1}})$
---
> [!warning]- Why it's not enough?
> Technically it should be enough, though it is redundant and can easily be optimized in its existence check.

## 5. Optimal approach

> [!info]- Complexity 
>time $O(n)$ / space $O(n)$
---
> [!info]- Idea
> Do the same as brute force, but optimize the duplicate check by using a hashmap.
---
> [!info]- Why it works (the key insight)
> Because.

## 6. Code
```python
# language: python
class Solution:
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		vert = [{} for i in range(9)]
		subgrid = [{} for i in range(9)]
		hori = [{} for i in range(9)]
		
		for i in range(9):
			for j in range(9):
				if board[i][j] == '.':
					continue
				if board[i][j] in hori[i]:
					return False
				hori[i][board[i][j]] = True
	
		for j in range(9):
			for i in range(9):
				if board[i][j] == '.':
					continue
				if board[i][j] in vert[j]:
					return False
				vert[j][board[i][j]] = True
				
		for k in range(9):
			shift_down = (k // 3) * 3
			shift_right = (k % 3) * 3
			for i in range(3):
				row = shift_down+i
				for j in range(3):
					col = shift_right+j
					if board[row][col] == '.':
						continue
					if board[row][col] in subgrid[k]:
						return False
					subgrid[k][board[row][col]] = True
					
		return True
```

## 7. Mistakes I actually made
- None

## 8. Edge cases to always check for this pattern
- [x] None

## 9. Related problems
- None

---

### Flashcards
