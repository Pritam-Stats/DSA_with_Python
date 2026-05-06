class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return (n*(n+1)//2) - sum(nums)

    def missingNumber_with_CyclicSort(self, nums: list[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            correctIdx = nums[i]
            if correctIdx == n: ##edge case
                nums.append(n)

            if nums[correctIdx] != nums[i]:
                nums[correctIdx], nums[i] = nums[i], nums[correctIdx]

            else:
                i += 1

        for i in range(n):
            if nums[i] != i:
                return i
        return n
