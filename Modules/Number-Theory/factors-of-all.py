def printFactorsOfAll(n):
    factors = [[] for _ in range(n)]

    ## it's a sieve like multiplier approach but this is very much memory heavy O(n log n) approach
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            factors[j-1].append(i)
    print(factors)

printFactorsOfAll(6)


def printFactorsForAll_SPF(n):
    # 1. build spf
    # Then for each number
        ## 2. prime factorize
        ## build the divisors from prime factorization and powers of the prime

    spf = list(range(n+1))
    i = 2
    while i*i <= n:
        for j in range(i*i, n+1, i):
            if spf[j] == j:
                spf[j] = i
        i += 1

    for num in range(1, n+1):
        divisors = [1]
        currNum = num

        #prime factorization
        while currNum> 1:
            p = spf[currNum]
            power = 0
            
            while currNum % p ==0:
                power += 1
                currNum //= p
            
            new_divs = []
            for d in divisors:
                for k in range(1, power+1):
                    new_divs.append(d * (p**k))
            divisors.extend(new_divs)
        print(f"{num} = {sorted(divisors)}")

printFactorsForAll_SPF(12)