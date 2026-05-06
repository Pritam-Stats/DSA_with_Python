'''
    Problem: https://leetcode.com/problems/max-consecutive-ones-iii/
'''

class Solution:
    def longestOnesBrue(self, nums: list[int], k: int) -> int:

        ##brute
        maxLen = 0
        n = len(nums)

        for i in range(n):
            zeroCnt = 0
            for j in range(i, n):
                if nums[j] == 0:
                    zeroCnt += 1
                if zeroCnt <= k:
                    maxLen = max(maxLen, j - i + 1)
                else:
                    break
        return maxLen
    '''
        TC: O(n2) -> Tle
    '''


    def longestOnesBetter(self, nums: list[int], k: int) -> int:
        '''
            Two pointer + sliding window
        '''
        n = len(nums)
        l, r = 0, 0
        maxLen = 0
        zeroCount = 0

        while r < n:
            if nums[r] == 0:
                zeroCount += 1

            while zeroCount > k:    #here we running this loop till we get zeroCount < k
                if nums[l] == 0:
                    zeroCount -= 1
                l += 1
            if zeroCount <= k:
                maxLen = max(maxLen, r-l+1)
            r += 1
        return maxLen
    '''
        TC: O(2n) theoretically
    '''

    def longestOnesOptimal(self, nums: list[int], k: int) -> int:
        n = len(nums)
        l, r = 0, 0
        zeroCount, maxLen = 0, 0

        while r < n:
            if nums[r] == 0:
                zeroCount += 1

            if zeroCount > k:   ## here we are keep running and and changing the l but maxLen won't get updated so while doesn't need here actually
                if nums[l] == 0:
                    zeroCount -= 1
                l += 1

            if zeroCount <= k:
                maxLen = max(maxLen, r-l+1)

            r += 1
        return maxLen
    '''
        TC: O(N)
    '''

        
