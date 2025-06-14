def maxProduct(nums:list) -> int:
    n = len(nums)
    left_to_right = 1
    right_to_left = 1
    maxP = float('-inf')

    for i in range(n):
        # the fix - edge case
        if left_to_right == 0:
            left_to_right = 1

        if right_to_left == 0:
            right_to_left = 1
            
        left_to_right *= nums[i]    #normal

        j = n-1 -i  #for backward calc
        right_to_left *= nums[j]

        maxP = max(maxP, left_to_right, right_to_left)
    return maxP

arr = [[2,3,-2,4], [-2,0,-1], [-3,0,1,-2]]   

for l in arr:
    print(maxProduct(l))    #6, 0, 1

# the last arr will return 1 without the FIX part