def findMaxAverage(nums: list[int], k: int) -> float:
    mav = float('-inf')
    i = 0
    while i <= len(nums)-k:
        mav = max(mav, sum(nums[i:i+k])/k)
        i += 1
    return mav

print(findMaxAverage(nums=[5], k=1))    #5
print(findMaxAverage(nums=[1,12,-5,-6,50,3], k=4))    #12.75

#O(NK)