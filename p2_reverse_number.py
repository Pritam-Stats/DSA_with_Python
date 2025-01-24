def reverse(self, x: int) -> int:
    sign = -1 if x <0 else 1
    x = abs(x)
    rev = 0
    
    while x > 0:
        last_digits = x % 10        #this will give the last digit. This will extract the remainder part
        rev = rev*10 + last_digits    #add the last digits one by one
        x = x // 10     #need to update x. remove the last digit. this will extract the integer part
    result = rev * sign
    if result < - 2**31 or result > 2**31 -1:
        result = 0
    return result

print(reverse(123))

print(reverse(-123))

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x <0 else 1

        num_str = str(abs(x))
        rev = num_str[::-1]

        result = int(rev) * sign

        if result < - 2**31 or result > 2**31 -1:
            result = 0


        return result
        

obj = Solution()
print(obj.reverse(-123))