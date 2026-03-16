def selectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        minId = i
        for j in range(i+1, n):
            if arr[j] < arr[minId]:
                minId = j
        arr[minId], arr[i] = arr[i], arr[minId]
    return arr

print(selectionSort([5, 4, 1, 1, 3, 2]))

def moveMaxToLast(arr):
    n = len(arr)
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i+1], arr[i] = arr[i], arr[i+1]
    return arr
## this part will move the max num to the last so we have to run this loop n-1 times to make the arr sorted


print(moveMaxToLast([5, 4, 1, 1, 3, 2]))
