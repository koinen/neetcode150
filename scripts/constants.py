from datetime import date

START_DATE = date(2026, 7, 16)
END_DATE = date(2026, 10, 16)

PROBLEM_MULTIPLIERS = {
    "easy": 1,
    "medium": 2,
    "hard": 3,
}

TOTAL_PROBLEMS = 150

TOTAL_WEIGHTED = 28 + 101*2 + 21*3

PROBLEM_DIR = "LeetCode"

PROBLEM_CATEGORIES = {
    "Arrays & Hashing": 9,
    "Two Pointers": 5,
    "Stack": 6,
    "Binary Search": 7,
    "Sliding Window": 6,
    "Linked List": 11,
    "Trees": 15,
    "Tries": 3,
    "Heap": 7,
    "Intervals": 6,
    "Greedy": 8,
    "Advanced Graph": 6,
    "Backtracking": 10,
    "Graphs": 13,
    "1-D DP": 12,
    "2-D DP": 11,
    "Bit Manipulation": 7,
    "Math & Geometry": 8,
}

PROBLEM_STATUSES = ["solved", "unsolved", "in_progress", "solved_with_hints", "solved_with_solution"]

README_PATH = "README.md"