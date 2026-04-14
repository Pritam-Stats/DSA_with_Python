def lessThanX(nums: list[int], q: int) -> int:
    nums.sort() #O(n logn)
    n = len(nums)
    for _ in range(q):  # O(q log n)
        ans = -1    #IMP
        x = int(input())
        l, r = 0, n-1
        while l<=r:         #(log n)
            m = (l+r)//2
            if nums[m] <= x:
                ans = m
                l = m+1
            else:
                r = m-1
        print(ans+1, "\n----------------------------------------")  

lessThanX([4, 3, 2, 1, 9, 8, 10, 5], 4)

'''
    Edge case: [4,5,6,7,8], x = 2
'''
# TC: O(n+q logn)