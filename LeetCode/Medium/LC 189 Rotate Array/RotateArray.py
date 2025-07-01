'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

'''


def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    if k > n:
        k = k % n
    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    #reverse complete array
    reverse(nums, 0, n-1)
    # reverse the first k
    reverse(nums, 0, k-1)
    # reverse the last n-k
    reverse(nums, k, n-1)

    return nums

# O(N), O(1)




def rotate2(nums: list[int], k: int) -> None:
    # if we make a new list
    # won't accept in leetcode O(N), O(N)
    n = len(nums)
    ans = [0]*n
    for i in range(n):
        ans[i] = nums[(i+k)%n]

    return ans

print("with inplace ", rotate(nums=[1,2,3,4,5,6,7], k = 3))
print("2nd method   ", rotate2(nums=[1,2,3,4,5,6,7], k = 3))
print("with inplace- ",rotate(nums=[-1,-100,3,99], k = 2))
print("2nd method    ",rotate2(nums=[-1,-100,3,99], k = 2))