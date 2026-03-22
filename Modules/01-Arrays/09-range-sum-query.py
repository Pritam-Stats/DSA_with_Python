'''  
    Author: Pritam
''' 
'''  
Problem: range sum query | CF w9 - array techniques A
Technique: Prefix sum
Intuition: store the cumulative sum
Mistake: 
Time: 
Space: 
'''    
def rangeSum(nums, l, r):
    n = len(nums)
    P = [0] * n
    currSum = 0     
    for i in range(n):
        currSum += nums[i]
        P[i] = currSum

    l, r = l-1, r-1
    if l == 0:
        return P[r]
    else:
        return P[r] - P[l]
    
arr = [1,2,3,4,5]
print(rangeSum(arr, 1, 3))  #6