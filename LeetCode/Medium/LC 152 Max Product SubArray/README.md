# 152. Maximum Product Sub array
- Link : [LeetCode 152](https://leetcode.com/problems/maximum-product-subarray/description/)

## Summary:
  - Given an array `nums` we have to find the sub-array which produce the largest product, and we are to return the product

### Key Logic
  - it's similar to max sub array sum but with a catch
  - Product can be different from the right to left and left to right, because of the position of non-positive values
  - So we have to go with two extra pointers as `left_to_right` and `right_to_left` then manage the `maxProduct`

#### One Edge Case What i missed
```
# the fix - edge case
    if left_to_right == 0:
        left_to_right = 1
    if right_to_left == 0:
        right_to_left = 1
```
  - This is needed otherwise once a product become 0 it can't come back even if there exist a subarray or a single positive element in the middle (a single element is also a sub array). 
  - Consider the array `nums = [-3,0,1,-2]`