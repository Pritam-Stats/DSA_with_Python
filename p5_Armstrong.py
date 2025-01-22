def isArmstrong(n: int) -> bool:
    '''
    An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

    Example 1:
    Input:N = 153
    Output:True
    Explanation: 1**3+5**3+3**3 = 1 + 125 + 27 = 153
    
    Example 2:
    Input:N = 371
    Output: True
    Explanation: 33+53+13 = 27 + 343 + 1 = 371
    '''
    og = n
    s = 0
    for i in str(n):
        s += int(i)**len(str(n))

    if s == og:
        return True
    else:
        return False

# result = isArmstrong(371)
# print(result)

# SECOND METHOD
def isArmstrong_Opt(n: int)-> bool:

    og = n
    count = 0
    s = 0
    
    #count the digits
    k = n
    while k > 0:
        count += 1
        k = k //10
    digits = count

    while n >0:
        i = n % 10      


isArmstrong_Opt(215)