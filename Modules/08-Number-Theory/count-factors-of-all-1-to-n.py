class CountFactors():

    def optimal(self, n: int):
        counts = [0]*n
        for i in range(1, n+1):
            for j in range(i, n+1, i):
                counts[j-1] += 1

        print(*counts)

        # TC: O(n log n)
        # SC: O(n)

#----------------------------------------------------------------------

    def nlog_n(self, n: int):
        """
        SC: O(n log n)
        TC: O(n log n)

        Args:
            n (int): last number
        """
        factors = [[] for _ in range(n)]

        for i in range(1, n+1):
            for j in range(i, n+1, i):
                factors[j-1].append(i)
    
        ans = []
        for facts in factors:
            ans.append(len(facts))
        # ans = map(str, ans)
        # print("\n".join(ans))
        print(*ans)


CountFactors().nlog_n(1000)
CountFactors().optimal(1000)