
## Given N, unset the right most bit

## Using Loop

def unsetRightMostSetBit(N):
    def checkIthBit(i):
        mask = 1 << i
        if N & mask == 0:
            return 0
        else:
            return 1


    def unsetIthBit(i):
        mask = ~(1 << i)
        return N & mask
    
    for i in range(31):
        if checkIthBit(i) == 1:
            ans = unsetIthBit(i)
            break
    print(ans)  #O(31)




## Without using a loop

def unset(N):
    return N&(N-1)  #O(1)

unsetRightMostSetBit(11)
print(unset(11))