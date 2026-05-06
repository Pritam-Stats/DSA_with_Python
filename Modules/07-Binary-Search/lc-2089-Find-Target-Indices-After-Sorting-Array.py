class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:

        nums.sort()
        n = len(nums)
        l, r = 0, n-1

        # first occ
        first = -1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                first = m
                r = m-1
            elif nums[m] > target:
                r = m-1
            else:
                l = m + 1

        if first == -1:
            return []

        # last occ
        l, r = 0, n-1
        last = first
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                last = m
                l = m+1
            elif nums[m] > target:
                r = m-1
            else:
                l = m + 1

        return [i for i in range(first, last+1)]
