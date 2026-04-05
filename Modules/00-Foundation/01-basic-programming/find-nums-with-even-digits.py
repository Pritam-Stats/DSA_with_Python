'''  
    Author: Pritam
''' 
'''  
Problem: 
Link/Platform: 
Technique: using log10 to calculate the number of digit in a number
Common Mistake: Not a mistake, but common instinct is to calculate lengths of nums by converting to string or separately
Time: O(N)
Space: O(1)
''' 
import math
def countOfEvenDigits(nums):
    count = 0
    for n in nums:
        if int(math.log10(n) + 1) % 2 == 0:
            count += 1

    return count
print(countOfEvenDigits([12, 345,2,6,7896]))    #2