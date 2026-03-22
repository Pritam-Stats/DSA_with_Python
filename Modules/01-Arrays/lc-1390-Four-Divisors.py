class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        def countDivisors(num):
            count = 0
            for d in range(1, int(num**0.5) + 1):
                if num % d == 0:
                    count += 2

                if d*d == num:
                    count -= 1
            return count

        filtered = [x for x in nums if countDivisors(x) == 4]

        if not filtered:
            return 0

        ans = 0

        def sumOfDivisors(num):
            factors = []
            for d in range(1, int(num**0.5) + 1):
                if num % d == 0:
                    factors.append(d)

                    if d*d != num:
                        factors.append(num//d)
            return sum(factors)

        for num in filtered:
            ans += sumOfDivisors(num)

        return ans
    


    def sumFourDivisorsOptimal(self, nums: list[int]) -> int:

        def sumofdivisorsIf4divs(num):
            count = 0
            divsums = 0

            for d in range(1, int(num**0.5) + 1):
                if num % d == 0:
                    count += 2
                    divsums += d + (num//d)

                    if d*d == num:
                        count -= 1
                        divsums -= d

                if count > 4:
                    return 0
            return divsums if count == 4 else 0

        return sum(sumofdivisorsIf4divs(num) for num in nums)
