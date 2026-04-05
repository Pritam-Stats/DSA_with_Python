def bubbleSort(arr):
    n = len(arr)
    for i in range(n):  #turns
        for j in range(n-i-1):  #scanning of the arr for each turn
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] #keep sending the mx at the end
    return arr


    
arr = [5,4,2,3,1,1]
print(bubbleSort(arr))