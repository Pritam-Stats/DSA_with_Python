from bisect import bisect_left


class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        ans = []
        sortedNums = sorted(nums)

        for x in nums:
            ans.append(bisect_left(sortedNums, x))

        return ans
