# Maximum Average Subarray I – LeetCode 643

**Problem Link:**  
[LeetCode 643 – Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75)

## Problem Summary

Given an array of integers `nums` and an integer `k`, find the contiguous subarray of length `k` that has the maximum average value, and return this value. The answer should be a floating-point number.

---

## 📄 Brute_Force_TLE.py

### 🔍 Approach:
- Iterate over all possible subarrays of length `k`.
- For each subarray, calculate its sum and keep track of the maximum average.

### 🧠 Concepts Used:
- Sliding window logic (without actual optimization)
- Subarray traversal
- Basic list slicing

### ⏱ Time Complexity:
- **O(n * k)** — For each possible starting index, a new sum of `k` elements is computed.

### 📦 Space Complexity:
- **O(1)** — Only a few variables are used; no extra data structures.

### ❌ Limitation:
- This solution is inefficient for large inputs and will result in **TLE (Time Limit Exceeded)** on LeetCode.

---

## 📄 Sliding_Window_Optimal.py

### 🔍 Approach:
- Use the **sliding window** technique.
- Calculate the sum of the first `k` elements to initialize the window.
- Slide the window across the array by removing the element going out and adding the one coming in.
- Track the maximum sum throughout the process.

### 🧠 Concepts Used:
- Sliding window (optimized)
- Prefix sum logic (implicitly)
- Constant time window update

### ⏱ Time Complexity:
- **O(n)** — Each element is processed once while sliding the window.

### 📦 Space Complexity:
- **O(1)** — Only a few variables are used.

### ✅ Advantage:
- Efficient and optimal for large datasets.
- Passes all test cases on LeetCode.

---

## ✅ Recommendation

Always prefer the **Sliding Window** method for problems involving fixed-size subarrays where you need to compute max/min/sum/average, as it reduces time complexity significantly.



---

# Maximum of all subarrays of Size k

Problem: https://www.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1
code : [here](./01-max-of-each-subarray-of-size-k.py)

## TC Analysis of this code

Let’s do a precise, line-by-line complexity audit.

⸻

Variables
	•	n = length of array
	•	k = window size

⸻

Step 1: Initial window build

for i in range(k):
    freq[arr[i]] = freq.get(arr[i], 0) + 1

	•	Runs k times
	•	Each hashmap operation = O(1) (amortized)

Cost:

O(k)

⸻

Step 2: First max computation

maxS = max(freq)

	•	freq can have up to k keys
	•	max() scans all keys

Cost:

O(k)

⸻

Step 3: Sliding window loop

for i in range(k, n):

Runs:
(n - k)
times

⸻

Inside each iteration

(a) Add new element

freq[arr[i]] = freq.get(arr[i], 0) + 1

→ O(1)

(b) Remove old element

freq[arr[i-k]] -= 1
if freq[arr[i-k]] == 0:
    del freq[arr[i-k]]

→ O(1)

(c) Recompute max

maxS = max(freq)

	•	Again scans up to k elements

→ O(k)

⸻

Total per iteration:

O(k)

⸻

Step 4: Total loop cost

(n - k) \cdot O(k) = O(nk - k^2)

⸻

Final Time Complexity

Combine everything:
O(k) + O(k) + O(nk - k^2)

Simplifies to:
O(nk)

⸻

Space Complexity

freq = {}

	•	Stores at most k elements

O(k)

⸻

Critical Observation (the bottleneck)

This line dominates everything:

max(freq)

You execute it:
	•	(n - k + 1) times
	•	Each time → O(k)

⸻

When does this become bad?

Scenario	Complexity
k small (e.g., 5)	~O(n)
k \approx n/2	~O(n²) ❌
k \approx n	~O(n²) ❌


⸻

> Why deque beats this? 
    Deque removes the need for: `max(freq)`

So instead of:
O(nk)
You get:
O(n)

⸻

Final takeaway
	•	Your logic is correct
	•	Your bottleneck is recomputing max repeatedly
	•	This is a classic case of:
“Correct approach, wrong data structure”


---

## TC Analysis of the 2nd Code

Good. That’s essentially correct. Let’s tighten it to a precise invariant-based understanding.

⸻

Refined Logic (clean mental model)

There are exactly two events that force work:

1. Incoming element dominates

arr[i] > current_max

→ New max found → O(1)

⸻

2. Outgoing element was the max

arr[i-k] == current_max

→ You lose information
→ Must recompute:

max(window) → O(k)


⸻

Otherwise
	•	Max is still inside window
→ No work needed (O(1))

⸻

Now let’s analyze complexity properly

Total iterations

Loop runs:
(n - k)

⸻

Cost per iteration

Case A: O(1)
	•	New element becomes max
	•	OR max stays inside window

Case B: O(k)
	•	When max leaves window

⸻

Key Question (this decides complexity)

👉 How often does Case B happen?

⸻

Best Case

Example:

[1, 2, 3, 4, 5, 6]

	•	Max keeps increasing
	•	Never recomputed

\text{Total} = O(n)

⸻

Worst Case (important)

Example:

[6, 5, 4, 3, 2, 1]

Every step:
	•	Max leaves window
	•	You recompute max

\text{Total} = (n-k) \cdot k = O(nk)

⸻

Average Case (intuition)
	•	Max doesn’t leave often
	•	So recomputation is rare

\approx O(n)

⸻

Important Examples to Understand

Example 1 (Best Case)

arr = [1,2,3,4,5], k = 3

Windows:
	•	[1,2,3] → 3
	•	[2,3,4] → 4
	•	[3,4,5] → 5

👉 Always Case A → O(n)

⸻

Example 2 (Worst Case)

arr = [5,4,3,2,1], k = 3

Windows:
	•	[5,4,3] → 5
	•	[4,3,2] → recompute
	•	[3,2,1] → recompute

👉 Always Case B → O(nk)

⸻

Example 3 (Mixed)

arr = [2,1,3,4,6,3,8,9,10,12,56], k = 4

	•	Sometimes max replaced
	•	Sometimes survives

👉 Mostly O(1) steps
→ behaves close to O(n)

⸻

Final Complexity Summary

Case	Complexity
Best	O(n)
Average	~O(n)
Worst	O(nk) ❌


⸻

Critical Insight (this is what matters)

Your solution is:

“Lazy recomputation”

	•	Avoids unnecessary work
	•	But cannot eliminate worst-case

⸻

Why interviewers reject this

Because:

Worst-case input is very easy to construct

And platforms like GFG / LeetCode include those cases intentionally → your TLE

⸻

What you should internalize
	•	You correctly optimized when to recompute
	•	But you still depend on recomputation

👉 Optimal solutions:
	•	Don’t recompute at all
	•	Maintain structure incrementally


---

---


