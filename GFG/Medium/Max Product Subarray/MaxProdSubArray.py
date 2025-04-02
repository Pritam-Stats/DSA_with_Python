def maxProduct(arr: list):

    '''
# [-2, 6, -3, -10, 0, 2]
	# considering this array we can observe if we keep on multiplying one item and update the maxProd this can give us answer
	# but another thing to observe is from i 0 to n and from i = n to 0 will give different results
	# because of the placement of 0 and negatives
    '''

    n = len(arr)  
    maxProd = float('-inf') 

    l_r = 1
    r_l = 1

    for i in range(n):
        if l_r == 0:
            l_r = 1

        if r_l == 0:
            r_l = 1

        l_r *= arr[i]

        j = n -i-1
        r_l *= arr[j]

        maxProd = max(maxProd, l_r, r_l)

    return maxProd

print(maxProduct(arr= [-2, 6, -3, -10, 0, 2]))  #180 [-10*-3*6]


