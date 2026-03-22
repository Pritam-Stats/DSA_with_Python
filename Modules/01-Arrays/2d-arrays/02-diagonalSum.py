'''  
Problem: 
Link/Platform: 
Technique: for loop
Core Idea & Intuition: sum the i, i pairs and the pairs where i != j (second diag). one single loop. dry run it'll be cleared
Invariant: n = m
Common Mistake: 2 loops is not needed, understand how the loop is being updated and col calculation 
Time: O(N)
Space: O(N)
''' 

def diagSum(arr2d):
    ds = 0
    n = len(arr2d)
    for i in range(n):
        ds += arr2d[i][i]
        j = n-i-1
        if i != j:
            ds += arr2d[i][j]
    

    print(ds)

diagSum([[1,2,3], [4,5,6], [7,8,9]])