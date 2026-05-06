def printFactors(n):
    factors = []
    i = 1
    while i*i <= n:
        if n % i == 0:
            factors.append(i)
        
        i += 1

    i -= 1
    while i*i >= 1:
        if n%i == 0 and i != n//i:
            factors.append(n//i)
        i -= 1
    print(*factors)

printFactors(36)

# O(sq n)