def maxSubArraySum(arr):
    # Your code here
    n = len(arr)
    #subarray is continuous
    maxSum = float('-inf')    #to handle the situation when all are neg so sum will be neg
    currSum = 0
    
    # let arr = [-2, -4]
    for i in range(n):
        currSum += arr[i]   # i = 0: -2 -> -4 (because currsum is 0)
        maxSum = max(maxSum, currSum)   #whichever is larger   #i = 0: replaced by -2
                                        # max(-2, -4) = -2
        
        if currSum < 0: #true for i =0
            currSum = 0 #assign currsum to 0 again. its better to start with 0 than neg (kadane's algo)
            
    return maxSum
            
        


