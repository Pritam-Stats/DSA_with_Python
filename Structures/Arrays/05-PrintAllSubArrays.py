arr = [1, 2, 3,4, 5]
def subArrays(arr: list):
    n = len(arr)
    for st in range(n):
        for end in range(st, n):
            print(*arr[st:end+1], end= ',  ')
        print()
subArrays(arr)