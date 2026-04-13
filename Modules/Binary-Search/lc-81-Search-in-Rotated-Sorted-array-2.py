


'''
    Problem: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
'''


class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        #find the k
        n = len(nums)
        k = 0
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                k = i
                break
        # return k
        #two sorted arrays [0,k] and [k+1, n-1]
        l, r = 0, k
        while l<= r:
            m = (l+r)//2
            if nums[m] == target:
                return True
            elif nums[m] > target:
                r = m-1
            else:
                l = m +1

        l = k+1
        r = n-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return True
            elif nums[m] > target:
                r = m-1
            else:
                l = m +1
        return False


