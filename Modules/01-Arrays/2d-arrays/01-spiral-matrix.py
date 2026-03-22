def spiral(arr2d):
    arr = []
    n, m = len(arr2d), len(arr2d[0])

    srow, erow, scol, ecol = 0, n-1, 0, m-1
    while (srow <= erow) and (scol <= ecol):
        #top - col change
        for j in range(scol, ecol+1):
            arr.append(arr2d[srow][j])
        srow += 1

        #right - row change
        for i in range(srow, erow+1):
            arr.append(arr2d[i][ecol])
        ecol -= 1

        #bottom - col change in reverse
        if srow <= erow:
            for j in range(ecol, scol-1, -1):
                arr.append(arr2d[erow][j])
            erow -= 1

        #left - row change in reverse
        if scol <= ecol:
            for i in range(erow, srow-1, -1):
                arr.append(arr2d[i][scol])
            scol += 1
        
    
    print(*arr)

arr2d = [[1,2,3, 4, 5, 6],
         [7, 8, 9, 10, 11, 12],
         [13, 14, 15, 16,17, 18]
         
        
        ]
spiral(arr2d)