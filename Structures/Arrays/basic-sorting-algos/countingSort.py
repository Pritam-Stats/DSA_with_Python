def countingSort2(arr):
    n = len(arr)
    '''  
        Author: Pritam
    ''' 
    '''  
    Problem: counting sort
    Technique: this is kind of counting sort but not exactly a counting sort algorithm
    Mistake: 
    Time: 
    Space: 
    ''' 
    freq = {}
    sortedArr = []

    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    mn = min(arr)
    mx = max(arr)
    for num in range(mn, mx+1):
        while freq.get(num, 0) > 0:
            sortedArr.append(num)
            freq[num] -= 1
    return sortedArr
arr = [5, 4, 1, 2]
print(countingSort2(arr))


def countingSort(arr):
    n = len(arr)
    k = max(arr)
    count = [0]*(k+1)

    for num in arr:
        count[num] += 1
    
    sortedArr = []
    for i in range(len(count)):
        sortedArr.extend([i]*count[i])
    return sortedArr


arr = [5, 4, 1, 2]
print(countingSort(arr))

