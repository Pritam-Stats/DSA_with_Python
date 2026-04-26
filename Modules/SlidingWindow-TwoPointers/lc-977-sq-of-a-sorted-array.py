

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        l, r = 0, n-1

        ans = [0]*n
        for i in range(n-1, -1, -1):
            if abs(nums[l]) >= abs(nums[r]):
                ans[i] = nums[l]**2
                l += 1
            else:
                ans[i] = nums[r]**2
                r -= 1
        return ans
        # O(n)


#------------------------------------------------------------------

    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        nums = map(lambda x: x**2, nums)
        return sorted(nums)

