def firstOcc(nums: list, target: int):
    n = len(nums)
    l, r = 0, n-1
    ans = -1
    while l<=r:
        m = (l+r)//2
        if nums[m] == target:
            ans = m
            r = m-1
        elif nums[m] > target:
            r = m-1
        else:
            l = m+1
    print(f"First Occ of {target} is at index: {ans}")


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
    print(f"Last Occ of {target} is at index: {ans}")

firstOcc([1, 2, 3, 3, 3, 4, 5], 3)

lastOcc([1, 2, 3, 3, 3, 4, 5], 3)

# TC: O(log2 N)