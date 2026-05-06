'''  
    Author: Pritam
''' 
'''  
Problem: https://leetcode.com/problems/sort-colors/description/
Technique: two (3) pointer
Intuition: track with mid, we know 2 will be at end, 0 at first but mid is the trick
Mistake: while loop condn
Time: O(n)
Space: O(1)
''' 

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l, mid, r = 0, 0, n-1

        while mid <= r:
            if nums[mid] == 0:
                nums[mid], nums[l] = nums[l], nums[mid]
                mid += 1
                l += 1
            elif nums[mid] == 2:
                nums[mid], nums[r] = nums[r], nums[mid]
                r -= 1
            else:
                mid += 1

        