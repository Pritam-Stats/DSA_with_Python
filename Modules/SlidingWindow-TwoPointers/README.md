# Maximum Average Subarray I (LC 643)
[Code](./LC-643-Max-Avg-SubArray-Solutions/)
- Problem: Fixed size subarray (k), maximize average ⇒ maximize sum

---

### Brute Force

- Check all subarrays of size k
- Compute sum each time

- Time: O(n * k)
- Space: O(1)

- Limitation: Recomputing sum repeatedly → TLE

---

### Sliding Window (Optimal)

- Maintain window sum of size k
- Slide:
  - add incoming
  - remove outgoing

- Time: O(n)
- Space: O(1)

- Key Idea:
  - Avoid recomputation
  - Reuse previous window

---

# Maximum of All Subarrays of Size k

### Approach 1 (HashMap + max)

- Maintain freq map of window
- Compute max(freq) every step

- Time:
  - Build: O(k)
  - Each step: O(k)
  - Total: O(nk)

- Space: O(k)

- Bottleneck:
  - `max(freq)` → O(k) repeated

---

### Approach 2 (Lazy Max Recompute)

- Track current max
- Recompute ONLY if max leaves window

---

### Cases

- New element > max → O(1)
- Max still inside → O(1)
- Max leaves → recompute → O(k)

---

### Complexity

- Best: O(n)
- Avg: ~O(n)
- Worst: O(nk)

---

### Insight

- Lazy optimization helps
- But worst case still bad

- Problem:
  - Still depends on recomputation

---

### Optimal Direction

- Use Deque
- Maintain decreasing order
- No recomputation

- Time: O(n)

---

# LC 424 — [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)
[Code](./lc-424-longest-repeating-char-replacement.py)
### Goal

- Longest substring where ≤ k replacements make all chars same

---

### Core Condition

- Valid window:
  - (window_size - maxF) ≤ k

---

### Approach

- Expand right
- Update freq + maxF
- If invalid → shrink left
- Track max length

---

### Key Trick

- Do NOT decrease maxF
- Stale maxF still works

---

### Why?

- It may allow slightly invalid window
- But never misses optimal answer

---

### Pattern

- Variable sliding window
- Constraint-based shrinking

---

### Complexity

- Time: O(n)
- Space: O(1)

---

### Invariant

- Maintain:
  - (r - l + 1) - maxF ≤ k
