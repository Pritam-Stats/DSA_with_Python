'''Check the CF Group for exact question'''

'''Given position array and k cows'''

def maxDistancePossible(pos: list[int], k: int) -> int:
    min_gap = 0
    max_gap = max(pos)//k

    def isPossible(arr, gap, k):
        cowsPlaced = 1
        prevPos = arr[0]
        m = len(pos)
        for i in range(1, m):
            if (arr[i] - prevPos) >= gap:
                cowsPlaced += 1
                prevPos = arr[i]
        return cowsPlaced >= k

    gaps = list(range(min_gap, max_gap+1))

    n = len(gaps)
    l, r = 0, n-1
    ans = -1
    while l<=r:
        m = (l+r)//2
        if isPossible(pos, gaps[m], k):
            ans = gaps[m]
            l = m+1
        else:
            r = m-1
    return ans


pos = [2, 5, 10, 16, 20, 29, 36]
k = 4

print(maxDistancePossible(pos, k))