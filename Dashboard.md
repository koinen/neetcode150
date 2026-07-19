
> [!warning] Setup
> Requires the **Dataview** plugin. Assumes your problem notes live in a folder called `LeetCode/` — change the path below if yours is different.

## Weakness by pattern

```dataview
TABLE
  length(rows) AS "Notes Count",
  round(sum(rows.sr-ease) / length(rows)) AS "Avg. Ease",
  min(rows.sr-ease) AS "Lowest Ease",
  max(rows.last-reviewed) AS "Last Reviewed"
FROM "LeetCode"
WHERE pattern
GROUP BY pattern as Pattern
SORT max(rows.last-reviewed) ASC
```

## Weakest individual notes

```dataview
TABLE
  pattern as "Pattern",
  difficulty as "Difficulty",
  sr-ease AS "Ease",
  sr-due AS "Next due"
FROM "LeetCode"
WHERE sr-ease
SORT sr-ease ASC
LIMIT 15
```

## Unsolved / needs revisit

```dataview
LIST
FROM "LeetCode"
WHERE status = "unsolved" OR status = "solved-slow"
```

## Coverage — patterns you haven't touched yet

- [x] Arrays & Hashing
- [x] Two Pointers
- [x] Stack
- [x] Binary Search
- [x] Sliding Window
- [ ] Linked List
- [ ] Trees
- [ ] Tries
- [ ] Heap/Priority Queue
- [ ] Intervals
- [ ] Greedy
- [ ] Backtracking
- [ ] Graphs
- [ ] 1-D DP
- [ ] 2-D DP
- [ ] Advanced Graphs
- [ ] Bit Manipulation
- [ ] Math & Geometry

## All notes (raw)

```dataview
TABLE
  number,
  difficulty,
  pattern,
  status,
  sr-ease,
  sr-due
FROM "LeetCode"
SORT number ASC
```
