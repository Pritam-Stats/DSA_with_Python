def myPow(x: float, n: int) -> float:
    if n == 0:
    #corner cases
        return 1.0
    if x == 0:
        return 0
    if x == 1:
        return 1
    if x == 1 or (x == -1 and n%2 == 0):
        return 1
    elif x == -1 and n%2 != 0:
        return -1
    # general solution of power which is running a for loop for all the number and keep multiplying x gives O(n) TC. Which will not be acceptable
    #here we have to get more optimal solution
    #BINARY EXPONENTIATION
    # for n = 5 we will run 5 iterations but binary for of 5 has (log_2 of 5 + 1) digits means 3 digits so we can optimize this by using 3 iterations instead of 5 iterations. which will make the solution o(log n) TC
    binForm = n
    ans = 1
    if n < 0:
        x = 1/x
        binForm = -binForm
    while binForm > 0:
        if binForm%2 == 1:
            ans *= x
        
        x *= x
        binForm //= 2
    return ans

print(myPow(9,3))


