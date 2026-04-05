def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        curr = arr[i]
        prev = i-1

        while (prev >= 0 and curr < arr[prev]):
            arr[prev], arr[prev+1] = arr[prev+1], arr[prev]
            prev -= 1
            
        arr[prev + 1] = curr

    return arr


arr = [5, 4, 1, 3, 2]
print(insertionSort(arr))