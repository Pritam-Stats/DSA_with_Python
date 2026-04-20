class primeFactors():
    def spf(self, n: int):  ## O(log log n)
        spf = [i for i in range(n+1)]
        i = 2
        while i*i <= n:
            if spf[i] == i: #prime
                for j in range(i*i, n+1, i):
                    spf[j] = min(spf[j], i)
            i += 1
        print(*spf)
        x = 12
        ans = []
        while x != 1:       # O(log n)
            ans.append(spf[x])
            x //= spf[x]
        print(*ans)


# -------------------------------------------------------------------------------
    def better(self, n:int):
        ans = []
        d = 2
        while d*d <= n:
            if n%d == 0:
                while n%d == 0:
                    ans.append(d)
                    n //= d
            if n > 1:
                ans.append(n)
            d += 1
        print(*ans)

# -------------------------------------------------------------------------------

    def brute(self, n:int):
        '''TC: O(n)'''
        ans = []
        for d in range(2, n+1):
            if n%d == 0:
                while n%d == 0:
                    ans.append(d)
                    n //= d
        print(*ans)


p = primeFactors()

p.brute(14)
p.better(14)
p.spf(20)