def selection(arr):
    n = len(arr)
    for i in range(n-1):
        minIdx = i
        for j in range(i+1, n):
            if arr[j] < arr[minIdx]:
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    return arr

print(selection([5, 4, 1, 1, 3, 2]))
        