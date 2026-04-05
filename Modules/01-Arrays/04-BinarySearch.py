arr = [2, 4, 6, 8, 10, 12, 14, 16]

def binarySearch(arr: list, target: int):
    n = len(arr)
    st, end = 0, n-1
    while st <= end:
        mid = (st + end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            #search left
            end = mid - 1
        else:
            #search right
            st = mid + 1
    return -1
print(binarySearch(arr, 44)) #1