from bisect import bisect_left
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)

        l, r = 0, n-1

        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m-1
            else:
                l = m+1

        return -1
    
    def search2(self, nums: list[int], target: int) -> int:
        n = len(nums)

        return bisect_left(nums, target)
    
s = Solution()
print(s.search([1,2,3,4,4,4,5], 4))
print(s.search2([1,2,3,4,4,4,5], 4))