arr = [1, 2, 3, 4, 5]

## With extra space
def revArray(arr):
    n = len(arr)
    copyArray = [0]*n
    for i in range(n):
        j = n - i - 1
        copyArray[i] = arr[j]

    for i in range(n):
        arr[i] = copyArray[i]

    return arr


### without extra space 
def swap(a: int, b: int) -> tuple:
    a, b = b, a
    return a, b


def revArrayTwoPointer(arr: list):
    n = len(arr)
    st, end = 0, n-1

    while st < end:
        swap(arr[st], arr[end])
        st += 1
        end -= 1
    return arr


print(revArray(arr))
print(revArrayTwoPointer(arr))

print(arr[::-1])    #creates a new reverse of the array using extra space
