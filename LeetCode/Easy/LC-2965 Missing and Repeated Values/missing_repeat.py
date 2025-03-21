# grid = [[9,1,7],[8,9,2],[3,4,6]]

def findMissingAndRepeatedValues(grid: list[list[int]]) -> list[int]:
    n = len(grid)   #square
    arr_1d = []
    

    for i in range(n):
        arr_1d += grid[i]

    freq = {}
    for nums in arr_1d:
        freq[nums] = freq.get(nums, 0) + 1
        
    a = 0   #REPEATED
    b = 0   #missing

    for num in range(1, n*n +1):
        if freq.get(num, 0) == 2:
            a = num
        # elif num not in arr_1d:
        elif freq.get(num, 0) == 0:
            b = num

    return [a, b]
    
    

            
print(findMissingAndRepeatedValues(grid = [[9,1,7],[8,9,2],[3,4,6]]))

## TC = O(N^2)

## Important thing - the get method of the dictionary
## The .get() method allows you to retrieve the value of a key in a dictionary. If the key exists, it returns the value. If the key doesn't exist, it returns a default value (which you specify, like 0).
