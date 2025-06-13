
def trappedWater(height:list) -> int:
    n = len(height)
    left_max = [0]*n
    right_max = [0] *n
    left_max[0] = height[0] #for this problem we -1 will also work, -inf wil work in py but will fail in cpp
    right_max[n-1] = height[n-1]

    
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i-1])
    # print(left_max)

    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i+1])

    # print(right_max)
    totalTrapped = 0
    for i in range(n):
        trapped = min(left_max[i], right_max[i]) - height[i]
        if trapped >0:
            totalTrapped += trapped
    return totalTrapped

    # O(N), O(N)
    # return trapped

heights = [[0,1,0,2,1,0,1,3,2,1,2,1], [4, 2,0,6,3,2,5], [4,2,0,3,2,5]]
for h in heights:
    print(trappedWater(height=h))

#ans = 6, 11, 9