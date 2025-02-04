'''
Problem - https://www.geeksforgeeks.org/problems/sum-of-all-divisors-from-1-to-n4738/1
'''

# def sumOfDivisors(n):
#     sums = 0
#     for i in range(1, n + 1):
#         divisors = []                         # Here SC is O(n)
#         for divs in range(1, i + 1):          # Here this had O(n^2) TC
#             if i% divs == 0:
#                 divisors.append(divs)
#         sums += sum(divisors)

#     return sums

def sumOfDivisors(n):
    sum_divisors = 0                        # SC is O(1). We are storing nothing extra, there are no other variable
    for d in range(1, n+1):     
        sum_divisors += (n // d) * d        # by n//d we will have the count of how many numbers will be divisible by that particular d in each step
                                            # and if we multiply that d to the the count we will have to total number of that divisor
                                            # By this approach we are not generating the divisors separately, which optimizing both the TC and SC.
    return sum_divisors                   # this ensures the time complexity to be O(n).


# The Breakdown of the approach
# d=1: 9//1=9 → 1*9=9

# d=2: 9//2=4 → 2*4=8

# d=3: 9//3=3 → 3*3=9

# d=4: 9//4=2 →4*2=8

# d=5:9//5=1 →5*1=5

# d=6:9//6=1 →6*1=6

# d=7:1 →7

# d=8:1 →8

# d=9:1 →9
# And we are summing at each step.


result = sumOfDivisors(9)
print(result)