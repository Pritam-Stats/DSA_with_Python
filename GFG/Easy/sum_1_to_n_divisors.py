'''
Problem - https://www.geeksforgeeks.org/problems/sum-of-all-divisors-from-1-to-n4738/1
'''

def sumOfDivisors(n):
    sums = 0
    for i in range(1, n + 1):
        divisors = []
        for divs in range(1, i + 1):
            if i% divs == 0:
                divisors.append(divs)
        sums += sum(divisors)

    return sums
result = sumOfDivisors(5)
print(result)