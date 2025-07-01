def transpose(matrix: list[list[int]]) -> list[list[int]]:
    n, m = len(matrix), len(matrix[0])
    transpose = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            transpose[j][i] = matrix[i][j]
    return transpose
    
    #O(nm)