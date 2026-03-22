def findMaxMin(arr: list):
    maxNum = arr[0]
    minNum = arr[0]
    n = len(arr)
    for i in range(n):
        if arr[i] > maxNum:
            maxNum = arr[i]
        if arr[i] < minNum:
            minNum = arr[i]

    print(f"Max of the array: {maxNum}\nMin of the array: {minNum}")

findMaxMin(arr = [1,2,3,4,0,7, 9, 2])
