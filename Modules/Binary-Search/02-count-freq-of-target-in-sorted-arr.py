'''
Idea: Get the first occ and last occ idx and calculate the length
'''

def firstOcc(nums: list, target: int):
    n = len(nums)
    l, r = 0, n-1
    ans = -1
    while l <= r:
        m = (l+r)//2
        if nums[m] == target:
            ans = m
            r = m-1
        elif nums[m] > target:
            r = m-1
        else:
            l = m+1
    return ans


def lastOcc(nums: list, target: int):
    n = len(nums)
    l, r = 0, n-1
    ans = -1
    while l <= r:
        m = (l+r)//2
        if nums[m] == target:
            ans = m
            l = m+1
        elif nums[m] > target:
            r = m-1
        else:
            l = m+1
    return ans


length = lastOcc([1, 2, 3, 3, 3, 4, 5], 3) - firstOcc([1, 2, 3, 3, 3, 4, 5], 3) + 1     # R-L+1 (SUBARRAY LENGTH)
print(length)

# TC: O(Q + log2 n)
# SC: O(1)
