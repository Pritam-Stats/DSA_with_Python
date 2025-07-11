- **Problem Link** : [LC 162 - Find Peak Element](https://leetcode.com/problems/find-peak-element/description/)
- **Date** : July 12, 2025
- **Topic** : [[Binary Search]] 
- **Difficulty** : #Medium 
- Expected Complexity: $O(log n)$

---
### Summary Description: 
Given a **0-indexed** integer array `nums`, find a peak element, and return its index.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbour that is outside the array.
- Peak element = Strictly greater than it's neighbour

#### Examples
- `[1, 2, 3, 1] -> 2` = 3 is the peak element
- `[1, 2, 1, 3, 5, 6, 4] -> 1`
## Strategy & Key Insights
 - TC suggests we need to use a Binary Search
 - we will compare `nums[mid]` with `nums[mid+1]`.
	 - if greater means the peak element is either the `mid` itself or in it's left.
	 - if lesser, peak is at the right.
- This approach works because the questions ask to return any of the peak element index.
- *If the question would ask to return only the first element then we have to use a LINEAR SEARCH APPROACH.*
- Think Simply, simple binary search, no need to complicate.
	- The problem asked to return any peak element not the first one, that's the catch and that's what supporting Binary Search.
## PseudoCode (Binary Search)
```Pseudocode
while l<r:
	mid = l+r/2
	if mid_val > mid+1_val:
		right = mid
	else:
		left = mid + 1

return anything b/w right left
```

## PseudoCode (Linear Search)
- Returns specifically the first peak element
```Python
n = len(nums)

for i in range(n):
	left = nums[i-1] if i>0 else float('-inf')
	right = nums[i+1] if i <n-1 else float('-inf')
	if nums[i] > left and nums[i] > right:
		return i

return 0
```
- Linear Search will return  1 for `nums=[1,2,1,3,5,6,4]`. Binary search can return any 1 or 5.