'''
    Problem: https://leetcode.com/problems/find-peak-element/
'''
'''
Key Intuition: if we are declining in a mountain means we already had a peak in our left,
if uphill, we will get a peak.
'''
class Solution:
    ## NeetCode
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, n-1

        while l<=r:
            m = l + ((r-l)//2)                #(l+r)//2 #another way to calculate mid which ensures out of bound
            # check if the left neighbour is greater
            if m > 0 and nums[m] < nums[m-1]:
                r = m-1
            elif m < n-1 and nums[m] < nums[m+1]:
                l = m+1
            else:
                return m



#--------------------------------------------------------------------------

class Solution:

    '''
        Best Solution. [Think like a mountain]
        TC: O(log n)
    '''
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, n-1

        while l < r:
            m = (l+r)//2
            if nums[m] > nums[m+1]:
                r = m
            else:
                l = m+1
        return l



#--------------------------------------------------------------------------
    '''
        Still brute force but Better Code
        TC: O(n)
    '''
    def findPeakElementBetter(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            left = nums[i-1] if i > 0 else float("-inf")
            right = nums[i+1] if i < n-1 else float("-inf")

            if nums[i] > left and nums[i] > right:
                return i

#--------------------------------------------------------------------------
    '''bad code: O(N)'''
    def findPeakElementBruteForce(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if n == 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1

        for i in range(1, n-1):
            if nums[i-1] < nums[i] > nums[i+1]:
                return i
        if nums[1] > nums[0]:
            return n-1
        else:
            return 0
