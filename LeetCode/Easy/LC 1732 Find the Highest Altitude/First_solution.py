def largestAltitude(gain: list[int]) -> int:
    alts = [0]*(len(gain)+1)
    
    for i in range(len(gain)):
        alts[i+1] = alts[i]+gain[i]
    return max(alts)  #both space and time O(n)


print(largestAltitude(gain = [-5,1,5,0,-7]))    #1
print(largestAltitude(gain = [-4,-3,-2,-1,4,3,2]))    #0