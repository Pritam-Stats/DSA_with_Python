def findFirstTrue(s: str):
    n = len(s)

    l, r = 0, n-1
    ans = -1
    while l<=r:
        m = (l+r)//2
        if s[m] == 'T':
            ans = m
            r = m-1
        else:
            l = m+1

    print(ans)

s = "FFFFTTTTT"
findFirstTrue(s)