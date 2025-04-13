def largestAltitude(gain: list[int]) -> int:
    current_alt = 0
    max_alt = 0
    for g in gain:
        current_alt += g
        max_alt = max(max_alt, current_alt) #improved space complexity to O(1)
    return max_alt


print(largestAltitude(gain = [-5,1,5,0,-7]))    #1
print(largestAltitude(gain = [-4,-3,-2,-1,4,3,2]))    #0


        