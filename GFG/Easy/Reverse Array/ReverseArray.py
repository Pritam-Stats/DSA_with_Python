def reverseArray(arr):
    # code here
    n = len(arr)
    
    for i in range(n//2):
        temp = arr[i]
        arr[i] = arr[n -1 -i]
        arr[n -1 -i] = temp
    
    
    return arr

## TC O(N)
## SC O(1)
print(reverseArray(arr=[1,2,3]))