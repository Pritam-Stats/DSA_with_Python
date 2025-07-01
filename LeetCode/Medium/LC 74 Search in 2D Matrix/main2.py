def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
        
    #Treat the matrix as a sorted arr
    n, m = len(matrix), len(matrix[0])
    l, r = 0, n*m -1
    while l<=r:
        mid = (l+r)//2
        midCell = matrix[mid//m][mid%m]
        if midCell == target:
            return True
        elif midCell > target:
            r = mid -1
        else:
            l = mid+1
    return False

# 0(log (m+n))