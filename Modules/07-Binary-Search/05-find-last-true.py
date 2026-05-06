def findLastTrue(s: str):
    n = len(s)

    ans = -1
    l, r = 0, n-1

    while l<=r:
        m = (l+r)//2
        if s[m] == 'T':
            ans = m
            l = m+1
        else:
            r = m-1

    print(ans)

s = "TTTTTTFFFFFF"

findLastTrue(s)