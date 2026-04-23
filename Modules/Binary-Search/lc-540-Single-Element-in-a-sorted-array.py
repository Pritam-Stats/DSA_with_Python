


# Link: https://leetcode.com/problems/single-element-in-a-sorted-array/

## Pattern to recognize: Before single element the numbers were appearing in EVEN-ODD index
## After the single element, pattern changes to ODD-EVEN.   

class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, n-1

        while l < r:
            mid = l + ((r-l)//2)
            if mid%2 != 0:
                mid -= 1
                
            if nums[mid] == nums[mid+1]:
                l = mid + 2
            else:
                r = mid
        #l and r will be in the same place
        return nums[r]
            

        

