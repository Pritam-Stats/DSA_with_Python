def findMaxAverage(nums: list[int], k: int) -> float:
    # sliding window
    window_sum = sum(nums[:k])
    max_sum = window_sum
    #slide the window
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k] #ultimately there will remain the sum k elements each time
        max_sum = max(window_sum, max_sum)
    return max_sum/k
        
print(findMaxAverage(nums=[5], k=1))    #5
print(findMaxAverage(nums=[1,12,-5,-6,50,3], k=4))    #12.75

#O(N)