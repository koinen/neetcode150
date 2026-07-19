>[!warning] This note is completely AI-generated.

> Rule of thumb: judges do roughly **`10^8` simple operations/sec** (C++; assume `~10^7-10^8` for Python). Take n from the constraints, find the row, and that's your ceiling — not a suggestion, a hard budget.

| n (input size)    | Required complexity             | Typical pattern                                 |
| ----------------- | ------------------------------- | ----------------------------------------------- |
| `n ≤ 10-12`       | $O(2^n)$, $O(n!)$               | brute force, permutations, backtracking         |
| `n ≤ 20-25`       | $O(2^n \cdot n)$                | bitmask DP, subsets                             |
| `n ≤ 100`         | $O(n^4)$                        | brute force nested loops, simple DP             |
| `n ≤ 500`         | $O(n^3)$                        | 3D DP, Floyd-Warshall                           |
| `n ≤ 2,000-5,000` | $O(n^2 \cdot log n)$            | sorting + nested loop                           |
| `n ≤ 10^4`        | $O(n^2)$                        | brute force pairs, simple DP over 2 indices     |
| `n ≤ 10^5 - 10^6` | $O(n \cdot log n)$              | sorting, heap, binary search, divide & conquer  |
| `n ≤ 10^6 - 10^8` | $O(n)$ or $O(n\cdot log(logn))$ | single pass, two pointer, sliding window, sieve |
| `n ≤ 10^9+`       | $O(log n)$ or $O(1)$            | binary search on answer, math/formula           |

## How to use this mid-problem

1. Find `n`'s upper bound in the constraints.
2. Match the row — that's your **complexity budget**, before you've even thought about the approach.
3. If your first idea (usually brute force) is a row _below_ the budget, you know upfront it'll TLE — don't bother submitting, go straight to optimizing.
4. If your idea matches or beats the row, you're probably fine — the "elegant" solution isn't always faster than what the constraints demand.

## Sneaky cases worth remembering

- **Two n's multiplied.** `n, m ≤ 1000` each isn't `n ≤ 1000` — it's effectively `n*m ≤ 10^6`, so $O(n\cdot m)$ is fine but $O(n^2 \cdot m)$ is not.
- **String problems**: length of string counts as your `n`. `s.length ≤ 10^5` means $O(n^2)$ substring generation (common brute force instinct) will TLE.
- **Number of queries * per-query cost matters, not just one alone.** `q ≤ 10^5` queries each costing $O(log n)$ → $O(q \cdot log n)$ total. Costing $O(n)$ each → $O(q\cdot n)$ → probably TLE if n is also large.
- **Graph problems**: n = nodes, but check edges (m) separately — $O(V + E)$ vs $O(V^2)$ diverges hard on sparse graphs.
- **DP with two dimensions**: $O(n*m)$ states, each $O(1)$ or $O(k)$ transition — multiply _all three_ together, not just $n \cdot m$, when checking against the budget.

## Quick gut-check examples

- `1 ≤ n ≤ 20` → almost certainly bitmask DP or brute-force subsets, don't overthink it
- `1 ≤ n ≤ 1000` → $O(n^2)$ nested loop is _intended_, not a fallback
- `1 ≤ n ≤ 10^5` → if your instinct is nested loops, that's your signal to look for sorting/two-pointer/hashmap instead
- `1 ≤ n ≤ 10^9` and no array given → answer is almost certainly math, binary search on the answer, or O(log n)