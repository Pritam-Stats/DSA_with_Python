class Solution:
    ## optimal
    def commonFactorsOptimal(self, a: int, b: int) -> int:
        '''
            Author: Pritam
        '''
        from math import gcd
        n = gcd(a, b)

        root = int(n**0.5)
        count = 0
        for d in range(1, root+1):
            if n % d == 0:
                count += 2
                if d*d == n:
                    count -= 1

        return count
    

    def commonFactorsBetter(self, a: int, b: int) -> int:
        if a > b:
            a, b = b, a  # a is smaller

        root = int(a**0.5)
        count = 0
        for d in range(1, root+1):
            if a % d == 0:      #wrong: if a%d == 0 and b%d == 0
                if b % d == 0:
                    count += 1

                if d*d != a and b % (a//d) == 0:
                    count += 1
        return count


    def commonFactorsBrute(self, a: int, b: int) -> int:
        if a > b:
            a, b = b, a  # a is smaller

        count = 0
        for d in range(1, a+1):
            if a % d == 0 and b % d == 0:
                count += 1
        return count


# imp test case
a = 850
b = 442
# ans 4
s = Solution()

print(s.commonFactorsBetter(a, b))
print(s.commonFactorsBrute(a, b))
print(s.commonFactorsOptimal(a, b))
