class Primes():
    def sieve_optimal(self, n: int):
        isprime = [True]*(n+1)
        isprime[0] = isprime[1] = False

        i = 2
        while i*i <= n:
            if isprime[i]:
                for j in range(i*i, n+1, i):
                    isprime[j] = False
            i += 1

        primes = []
        for i in range(n+1):
            if isprime[i]:
                primes.append(i)
        return len(primes)
        print(*primes)



    def sieve(self, n: int):
        isprime = [True]*(n+1)
        isprime[0] = isprime[1] = False

        for i in range(2, n+1):
            for j in range(2*i, n+1, i):
                if isprime[i]:
                    isprime[j] = False
        primes = []
        for i in range(n+1):
            if isprime[i]:
                primes.append(i)
        # print(*primes)
        return len(primes)

    def multiplierApproach(self, n: int):
        primes = []
        counts = [0]*(n-1)
        for i in range(2, n+1):
            for j in range(i, n+1, i):
                counts[j-2] += 1
        
        for i in range(2, n+1):
            if counts[i-2] == 1:
                primes.append(i)
        return len(primes)
        print(*primes)

print(Primes().multiplierApproach(100000))
print(Primes().sieve(100000))
print(Primes().sieve_optimal(100000))