def binary(n):
    ans = []
    curr = 1
    while curr <= n:
        curr *= 2
    curr //= 2

    while n > 0:
        if curr <= n:
            n -= curr
            ans.append(str(1))
        else:
            ans.append(str(0))
        curr //= 2
    print("0b"+"".join(ans))

binary(4)
print(bin(4))