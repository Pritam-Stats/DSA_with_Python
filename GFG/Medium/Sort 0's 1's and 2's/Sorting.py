def sort012(arr: list):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

print(sort012(arr=[0,1,2,2,2,1,2,0,0,0,1,2,1,1,2]))
print(sort012(arr=[2,1,0,1,2,0,1,1,0,2]))

# O(n), O(1)