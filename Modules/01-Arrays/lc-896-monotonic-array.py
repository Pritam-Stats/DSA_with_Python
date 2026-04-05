class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        n = len(nums)

        if nums[0] >= nums[n-1]:
            # either decreasing or equal
            for i in range(1, n):
                if nums[i-1] < nums[i]:
                    return False
            return True
        else:
            for i in range(1, n):
                if nums[i-1] > nums[i]:
                    return False
            return True
        
    def isMonotonicBetter(self, nums: list[int]) -> bool:
        n = len(nums)
        increasing = True
        decreasing = True

        for i in range(1,n):
            if nums[i-1] > nums[i]:
                increasing = False
            elif nums[i-1] < nums[i]:
                decreasing = False
        
        return increasing or decreasing
    
    def isMonotonicBest(self, nums: list[int]) -> bool:
        n = len(nums)
        direction = 0
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                if direction == 1:
                    return False
                direction = -1
            elif nums[i-1] < nums[i]:
                if direction == -1:
                    return False
                direction = 1
        return True


