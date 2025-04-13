
# LeetCode 1732 Largest Altitude Solution

## Problem Overview
The task is to find the highest altitude reached after applying a series of altitude changes starting from 0. We are provided with an integer array `gain` where each element represents the change in altitude from the previous position.

For more details, you can refer to the problem on LeetCode: [Find the Highest Altitude](https://leetcode.com/problems/find-the-highest-altitude/?envType=study-plan-v2&envId=leetcode-75)

## Approach 1: Using an Array to Track All Altitudes

### Approach:
- Create an array `alts` to store the altitude at each step, including the starting point at altitude `0`.
- Iterate through the `gain` array and update the altitude at each step.
- After processing all the altitude changes, return the maximum value from the `alts` array.

### Time Complexity:
- **O(n)**, where `n` is the length of the `gain` array. We traverse the `gain` array once.

### Space Complexity:
- **O(n)**, since an additional array `alts` of size `n+1` is created to store the altitude at each step.

---

## Approach 2: Optimized Space Solution

### Approach:
- Initialize two variables: `current_alt` (starting from 0) to track the current altitude, and `max_alt` (also starting from 0) to track the highest altitude encountered.
- Iterate through the `gain` array, updating the `current_alt` at each step and adjusting the `max_alt` accordingly.
- At the end of the loop, return the `max_alt`, which contains the highest altitude reached.

### Time Complexity:
- **O(n)**, where `n` is the length of the `gain` array. The algorithm makes a single pass through the `gain` array.

### Space Complexity:
- **O(1)**, as only a constant amount of extra space is used for `current_alt` and `max_alt`.

---

## Conclusion
- **Approach 1** is easy to understand but has a higher space complexity due to storing all altitudes.
- **Approach 2** is more space-efficient, using only two variables to track the current and maximum altitudes, making it the preferred solution for larger inputs.

