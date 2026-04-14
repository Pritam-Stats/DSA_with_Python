from bisect import bisect_left
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)

        l, r = 0, n-1

        while l <= r:
            m = (l+r)//2

            if nums[m] >= target:
                r = m-1
            else:
                l = m+1

        return l

    def searchInsert2(self, nums: list[int], target: int) -> int:
        return bisect_left(nums, target)
