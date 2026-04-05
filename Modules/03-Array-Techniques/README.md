
# Maximum Subarray Sum (Kadanes + Subarray)

- Maintain:
  - `currSum` → current subarray sum
  - `newStart` → potential start
  - `l, r` → best indices

- For each index:
  - add element to `currSum`
  - if `currSum > maxSum` → update `(l, r)`
  - if `currSum < 0` → reset and set `newStart = i + 1`

- Critical:
  - update before reset (handles all-negative case)

- Pattern: discard negative prefix

- Time: O(n), Space: O(1)


# Print the subarray as well with the sum - kadanes extended
- Track 3 things:
    - currSum → current subarray sum
    - newStart → start index of current candidate
    - l, r → best subarray indices
- At each index i:
	- Add nums[i] to currSum
	- Check first: if currSum > maxS → update maxS, l = newStart, r = i
	- Then reset: if currSum < 0 → set currSum = 0, newStart = i + 1
- Critical detail:
    - Always update before reset, otherwise all-negative cases break
- Why reset at i+1:
    - Negative sum means current subarray is useless → next subarray must start fresh
- Edge case:
  - Works correctly for all-negative arrays only if update happens before reset
- Time: O(n)
- Space: O(1)


# Vowel Strings in Ranges (LC 2559)

- Convert condition → binary array (1 if valid word else 0)
- Build prefix sum: `ps[i] = count till i`
- Query:  
  - `l == 0 → ps[r]`  
  - else → `ps[r] - ps[l-1]`
- Pattern: range query → prefix sum
- Time: O(n + q), Space: O(n)



# Max Vowels in Substring of Size K (LC 1456)

- Fixed window size → sliding window
- Maintain running count
- Add right, remove left
- Track max
- Avoid recomputation (`O(nk)` → `O(n)`)
- Pattern: fixed k → sliding window
- Time: O(n), Space: O(1)



# Sum of Even Numbers After Queries (LC 985)

- Maintain running even sum
- For each query:
  - if old even → subtract
  - update value
  - if new even → add
- Only one element changes → incremental update
- Pattern: update global state locally
- Time: O(n + q), Space: O(1)