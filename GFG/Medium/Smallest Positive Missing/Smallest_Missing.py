def missingNumber(arr: list) -> int:
    #Your code here
    # arr.sort()    # Not Optimized approach
    n = len(arr)
    
    # place the x-value at x-th place (x-1) index, if 1 is there place at the 1st place (i = 0)
    # x = arr[i]
    for i in range(n):
        while 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:   #2 should be in the 2nd (i =1) place
            # just swap 
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] -1]

    # we have to go through the and check each no
    for i in range(1, n+1): #since we need to check 1 to n
        if arr[i-1] != i:
            return i
            
    return n+1  #means all number is present
            
    
    #TC - O(N), SC- O(1)


print(missingNumber([2, -3, 4, 1, 1, 7]))  # Output: 3
print(missingNumber([1, 2, 0]))            # Output: 3
print(missingNumber([3, 4, -1, 1]))        # Output: 2




# Not Optimized. TC - O(n log n) SC- O(1)
# def missingNumber(arr):
#     #Your code here
#     arr.sort()  #TC - O(n log n)
#     n = len(arr)
    
#     ans = 1     #since smallest POSITIVE
    
#     for i in range(n):
#         if arr[i] == ans:   #if ans is there in the array keep on increasing by 1
#             ans += 1
            
#         elif arr[i] > ans:  #simply return the prev stored ans
#             break
    
#     return ans
