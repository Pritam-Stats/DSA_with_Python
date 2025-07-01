def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    #row wise bs
    n = len(matrix)    #rows
    m = len(matrix[0]) #cols
    for i in range(n):
        l, r = 0, m-1
        while l<=r:
            mid = (l+r) // 2
            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] > target:
                r = mid-1
            else:
                l = mid + 1
    return False
    #O(n log m)
    


#2nd approach
def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    n = len(matrix)
    m = len(matrix[0])
    row, col = 0, m-1   #start  #move left or down
    while row < n and col >=0:
        cell = matrix[row][col]
        if cell == target:
            return True
        elif cell < target:
            #move down
            row += 1
        else:
            #move left
            col -= 1
    return False
    #O(m+n)    #at worst we need to travel L shaped (m+n)

