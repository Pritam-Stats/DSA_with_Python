#User function Template for python3

def getMinDiff(arr,k):
    # code here
    n = len(arr)
    if n == 1:
        return 0
        
    arr.sort()
    
    
    ans = arr[n-1] - arr[0]
    for i in range(1, n):
        if arr[i]-k <0:
            continue
        
        minHeight = min(arr[0] + k, arr[i] - k)
        maxHeight = max(arr[n-1] - k, arr[i-1] + k)
        
        ans = min(ans, maxHeight - minHeight)
        
    return ans
            
                


print(getMinDiff(arr= [14,2,3,4,9,8], k=2))