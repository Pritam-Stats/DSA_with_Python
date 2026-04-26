def representN(N:int):
    #1. Find the nearest power of 2 of N
    curr = 1
    while curr <= N:
        curr *= 2
    curr = curr//2  #nearest power
    ans = []
    #start printing the representation from curr
    while N>0:
        if curr <= N:
            ans.append(curr)
            N -= curr   #remaining
        curr //= 2
    
    print(*ans)
representN(int(input()))
