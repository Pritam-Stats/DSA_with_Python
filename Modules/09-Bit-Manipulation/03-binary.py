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


def binary_bit(N:int):
    def checkIthBit(i):
        mask = 1 << i
        return (N & mask)
    ans = ["0b"]
    for i in range(30, -1, -1):
        if checkIthBit(i) == 0:
            ans.append(str(0))
        else:
            ans.append(str(1))
    print(''.join(ans))
print(bin(4))
binary_bit(4)