def printFactorsOfAll(n):
    factors = [[] for _ in range(n)]

    for i in range(1, n+1):
        for j in range(i, n+1, i):
            factors[j-1].append(i)
    print(factors)

printFactorsOfAll(6)