class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        nums = []
        for x in grid:
            nums += x
        n = len(nums)
        i = 1
        while i <= n:
            correctIdx = nums[i-1] -1

            if nums[correctIdx] != nums[i-1]:
                #swap
                nums[correctIdx], nums[i-1] = nums[i-1], nums[correctIdx]
            
            else:
                i+=1
        # return nums

        for i in range(1, n+1):
            if nums[i-1] != i:
                return [nums[i-1], i]

