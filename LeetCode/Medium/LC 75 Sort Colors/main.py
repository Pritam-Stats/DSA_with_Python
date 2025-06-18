def sortColor(nums: list) -> list:
    n = len(nums)
    low, mid, high = 0, 0, n-1  #imagine 3 parts, mid is our main pointer
    while mid < high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1

        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1
    return nums


print(sortColor(nums = [0, 1, 0, 2, 2, 1, 1, 0, 0]))