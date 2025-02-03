def lcmAndGcd(a : int, b : int) -> list[int]:
    # code here
    s_a = set()
    s_b = set()
    
    i, j = 1, 1
    while i<= a:
        if a%i == 0:
            s_a.add(i)
        i += 1
    while j <= b:
        if b %j == 0:
            s_b.add(j)
        j += 1

    gcd = max(s_a.intersection(s_b))
    # lcm = (a * b)//gcd
    
    #lcm

    lcm = max(a, b)     #lcm will be always greater than or equal to the max

    while True:
        if lcm % a == 0 and lcm % b == 0:
            break       #leave the while block
        lcm += 1        #otherwise keep on checking the next value

    return [lcm, gcd]

result = lcmAndGcd(14,8)
print(result)