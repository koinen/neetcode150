import os
import frontmatter
from datetime import date, timedelta
from datetime import date
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

# --- constants ---------------------------------------------------------
START_DATE = date(2026, 7, 16)
END_DATE = date(2026, 10, 16)

PROBLEM_MULTIPLIERS = {
    "easy": 1,
    "medium": 2,
    "hard": 3,
}

PROBLEM_DIFFICULTIES = {
    "easy": 28,
    "medium": 101,
    "hard": 21,
}

TOTAL_PROBLEMS = 150

TOTAL_WEIGHTED = sum(PROBLEM_DIFFICULTIES[difficulty] * multiplier for difficulty, multiplier in PROBLEM_MULTIPLIERS.items())

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

PROBLEM_STATUSES = ["solved", "unsolved", "in-progress", "solved-with-hints", "solved-with-solution"]

SCRIPTS_DIR = Path(__file__).parent
TEMPLATE_NAME = "progress_block.md.j2"

PROGRESS_MD = Path(__file__).parent.parent / "README.md"
MARK_START = "<!-- PROGRESS:START -->"
MARK_END = "<!-- PROGRESS:END -->"

def get_metadata(file_path) -> dict:
    with open(file_path, "r", encoding="utf-8") as f:
        post = frontmatter.load(f)
    return post.metadata

def load_problems_metadata() -> list[dict]:
    """
    Load the metadata of all problems in the vault.
    Each problem is a markdown file with frontmatter metadata.
    """
    problems = []
    for category in PROBLEM_CATEGORIES.keys():
        category_path = os.path.join(PROBLEM_DIR, category)
        if os.path.exists(category_path):
            for note in os.listdir(category_path):
                note_path = os.path.join(category_path, note)
                if os.path.isfile(note_path):
                    metadata = get_metadata(note_path)
                    problems.append(metadata)
    return problems

def get_last_active_date(problems_metadata: list[dict]) -> date | None:
    if not problems_metadata:
        return None
    dates = [problem.get("date-first-attempt") for problem in problems_metadata if "date-first-attempt" in problem]
    if not dates:
        return None
    return max(dates)

def get_streak(problems_metadata: list[dict]) -> int:
    """
    Calculate the current streak of consecutive days with activity.
    """
    if not problems_metadata:
        return 0

    # Extract dates and sort them in descending order
    dates = sorted({problem.get("date-first-attempt") for problem in problems_metadata if "date-first-attempt" in problem}, reverse=True)
    print(f"Dates for streak calculation: {dates}")
    streak = 0
    today = date.today()

    for i, d in enumerate(dates):
        if i == 0:
            # Check if the most recent date is today or yesterday
            if d == today or d == today - timedelta(days=1):
                streak += 1
            else:
                break
        else:
            # Check for consecutive days
            if d == dates[i - 1] - timedelta(days=1):
                streak += 1
            else:
                break

    return streak

def get_diff_counts(problems_metadata: list[dict]) -> dict:
    """
    Count the number of problems solved in each difficulty category.
    example shape:
    {
        "easy": {
            "solved": 10,
            "total": 28
        }
    }
    """
    counts = {difficulty: {
        "solved": 0,
        "total": total
    } for difficulty, total in PROBLEM_DIFFICULTIES.items()}

    for problem in problems_metadata:
        status = problem.get("status")
        difficulty = problem.get("difficulty").lower()
        if status.startswith("solved") and difficulty in counts:
            counts[difficulty]["solved"] += 1

    return counts

def get_pattern_counts(problems_metadata: list[dict]) -> dict:
    """
    example shape: 
    {
        "Arrays & Hashing": {
            "total": 9,
            "solved": 5,
            "unsolved": 3,
            "in_progress": 1,
            "solved_with_hints": 0,
            "solved_with_solution": 0
        },
        ...
    }
    """
    pattern_counts = {}
    for category in PROBLEM_CATEGORIES.keys():
        counts = {"total": PROBLEM_CATEGORIES[category]}
        for status in PROBLEM_STATUSES:
            counts[status] = 0

        for problem in problems_metadata:
            if problem.get("pattern") == category:
                status = problem.get("status")
                if status in counts:
                    counts[status] += 1

        pattern_counts[category] = counts

    return pattern_counts

def get_total_problems(problems: dict) -> int:
    return sum(counts["total"] for counts in problems.values())

def compute_stats(pattern_counts, dif_counts) -> dict:
    """
    Turn the raw problem log into everything the template needs.
    Fill in each TODO — the dict shape at the bottom must stay intact
    since render_and_write() depends on these exact keys.
    """
    today = date.today()

    # days_elapsed = days since START_DATE (min 1 to avoid /0)
    days_elapsed = (today - START_DATE).days + 1

    # days_remaining = days until TARGET_DATE (min 0)
    days_remaining = max(0, (END_DATE - today).days)

    # raw_done = len(problems)
    raw_done = sum(pattern_counts.get(name, {}).get("solved", 0) for name in pattern_counts)

    # weighted_done = sum of WEIGHTS[difficulty] across problems
    weighted_done = sum(dif_counts[dif]["solved"] * PROBLEM_MULTIPLIERS[dif] for dif in dif_counts)

    # pace_raw = raw_done / days_elapsed
    pace_raw = raw_done / days_elapsed

    pace_weighted = weighted_done / days_elapsed

    # required_pace = (TOTAL_PROBLEMS - raw_done) / days_remaining
    #       (guard against days_remaining == 0)
    required_raw_pace = (TOTAL_PROBLEMS - raw_done) / days_remaining

    required_weighted_pace = (TOTAL_WEIGHTED - weighted_done) / days_remaining

    pattern_done_percentage = {pattern: ((counts["solved"] + counts["solved_with_hints"] + counts["solved_with_solution"]) / counts["total"] * 100) if counts["total"] > 0 else 0 for pattern, counts in pattern_counts.items()}

    return {
        "days_elapsed": days_elapsed,
        "days_remaining": days_remaining,
        "raw_done": raw_done,
        "pace_raw": pace_raw,
        "required_raw_pace": required_raw_pace,
        "total_problems": TOTAL_PROBLEMS,
        "percentage_raw": raw_done / TOTAL_PROBLEMS * 100,
        "weighted_done": weighted_done,
        "pace_weighted": pace_weighted,
        "required_weighted_pace": required_weighted_pace,
        "total_weighted": TOTAL_WEIGHTED,
        "percentage_weighted": weighted_done / TOTAL_WEIGHTED * 100,
        "pattern_done": pattern_counts,
        "pattern_done_percentage": pattern_done_percentage
    }

# --- this part is the actual jinja2 demo, fully wired up ----------------
def render_block(stats: dict, pattern_counts: dict, problems_metadata: list[dict]) -> str:
    env = Environment(
        loader=FileSystemLoader(SCRIPTS_DIR),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    template = env.get_template(TEMPLATE_NAME)

    context = {
        **stats,
        "pattern_counts": pattern_counts,
        "total_days": (END_DATE - START_DATE).days,
        "streak": get_streak(problems_metadata),
        "last_active_date": get_last_active_date(problems_metadata),
        "diff_counts": get_diff_counts(problems_metadata)
    }
    print(sorted(context.keys()))
    return template.render(**context)

def update_markdown(new_block: str):
    if not PROGRESS_MD.exists():
        PROGRESS_MD.write_text(new_block + "\n")
        return

    text = PROGRESS_MD.read_text()
    if MARK_START in text and MARK_END in text:
        pre = text.split(MARK_START)[0]
        post = text.split(MARK_END)[1]
        text = pre + new_block + post
    else:
        text = text.rstrip() + "\n\n" + new_block + "\n"
    PROGRESS_MD.write_text(text)


def main():
    problems_metadata = load_problems_metadata()
    pattern_counts = get_pattern_counts(problems_metadata)
    stats = compute_stats(pattern_counts, get_diff_counts(problems_metadata))
    block = render_block(stats, pattern_counts, problems_metadata)
    update_markdown(block)
    print("progress.md updated.")


if __name__ == "__main__":
    main()
