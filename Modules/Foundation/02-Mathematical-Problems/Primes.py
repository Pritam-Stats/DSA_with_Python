class Primes:
    def isPrime(self, n: int) -> bool:
        if n <= 1:
            return False
        if n== 2 or n == 3:
            return False
        
        if n%2 == 0 or n%3==0:
            # This will allow us to jump 6th step each time, since 2 and 3 are already checked
            return False
        
        i = 5   #we can start from 5 since the num which is divisible by 4 will be divisible by 2 as well which has already been checked.
        while i*i <= n:
            if n % i == 0 or n % (i+2) == 0:
                return False
            i += 6

        return True


    def isPrime_Sieve(self, n: int)->int:
        '''Count till n (included)'''
        if n < 2:
            return 0
        prime = [True] * (n+1)
        prime[0] = prime[1] = False
        p = 2

        while p*p <= n:
            if prime[p]:
                for i in range(p*p, n+1, p):
                    prime[i] = False
            
            p += 1
        print(f"Total number of primes under {n} is: {sum(prime)}")

        res = []
        for p in range(2, n+1):
            if prime[p]:
                res.append(p)
        return res

p = Primes()
print(p.isPrime(7))
print(p.isPrime_Sieve(7))
print(p.isPrime_Sieve(10))
print(p.isPrime_Sieve(0))   #this is an edge case

