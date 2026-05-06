def power(n):
    curr = 1
    i = 1
    while i <= n:
        # print(curr)
        curr *= 2
        i += 1
    print(curr)

def power2(n):
    print(1 << n)   #left shift O(1)

power(4)
power2(4)