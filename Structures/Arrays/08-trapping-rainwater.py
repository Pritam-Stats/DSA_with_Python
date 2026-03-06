'''  
    Author: Pritam
''' 
'''  
Problem: 
Link/Platform: 
Technique: Brute, Create two aux arrays to store rightMax and LeftMax for each bar
Core Idea & Intuition: water can only be trapped inside a valley created by the bars
Invariant: 
Common Mistake: we have to have the largest bars on the left and right not the immediate larger
Time: O(n)
Space: O(n)
'''
def trapped(arr):
    n = len(arr)
    if n < 3:
        return 0
    water = 0
    lm = [0]*n
    for i in range(1, n):
        lm[i] = (max(lm[i-1], arr[i-1]))
    
    #right max
    rm = [0]*n
    for j in range(n-2, -1, -1):
        rm[j] = max(rm[j+1], arr[j+1])

    for i in range(1, n-1):
        wateri = (min(lm[i], rm[i]) - arr[i])
        if wateri < 0:
            wateri = 0
        water += wateri
    return water




'''  
    Author: Pritam
''' 
'''  
Problem: 
Link/Platform: 
Technique: 2 pointer (Optimal)
Core Idea & Intuition: 
Invariant: At every step, the side with the smaller current height (or smaller max) determines the possible water level at that side. 
Common Mistake: 
Time: O(n)
Space: O(1)
'''     

def trapped2(height):
    totalWaterTrapped = 0
    n = len(height)
    if n<3:
        return 0
    l, r = 0, n-1

    maxL, maxR = height[l], height[r]
    while l<r:
        if height[l] < height[r]:
            if height[l] > maxL:
                maxL = max(maxL, height[l])
            else:
                totalWaterTrapped += maxL - height[l]
            l += 1
        else:
            if height[r] > maxR:
                maxR = max(maxR, height[r])
            else:
                totalWaterTrapped += maxR - height[r]
            r -= 1
    return totalWaterTrapped



    return totalWaterTrapped



arr = [4,2,0,6,3,2,5]
print(trapped(arr))
print(trapped2(arr))
print(trapped([1,2,3,4,5])) #0
print(trapped2([1,2,3,4,5])) #0
