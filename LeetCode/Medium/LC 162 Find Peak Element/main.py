def peakElement(nums: list[int]) -> int:
    """LC 162
    Args:
        nums (list[int]): array
    Returns:
        int: returns the index of the peak element (O based index)
    Complexity: o(log n)
    """
    n = len(nums)
    left, right = 0, n-1
    while left < right:
        mid = (left + right)//2
        if nums[mid] > nums[mid + 1]:
            #peak is either at the mid or left
            right = mid
        else:
            left = mid + 1

    return left

if __name__ == "__main__":
    print("Using Binary Search.")
    print(peakElement(nums=[1]))    #0
    print(peakElement(nums=[1,2,3,1]))    #2
    print(peakElement(nums=[1,2,1,3,5,6,4]))    # 1 or 5


def findPeakElement(nums: list[int]) -> int:
    n = len(nums)
    for i in range(n):
        left = nums[i-1] if i>0 else float('-inf')
        right = nums[i+1] if i <n-1 else float('-inf')

        if nums[i] > left and nums[i] > right:
            return i
    return 0

if __name__ == "__main__":
    print("By Linear Search.")
    print(findPeakElement(nums=[1]))    #0
    print(findPeakElement(nums=[1,2,3,1]))    #2
    print(findPeakElement(nums=[1,2,1,3,5,6,4]))    # 1 
