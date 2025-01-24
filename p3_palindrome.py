def isPalindrome(self, x: int) -> bool:
    if x < 0:
        return False
    else:
        rev = 0
        original = x        #save the x as we will be updating x
        
        while x > 0:
            last_digit = x % 10
            rev = rev*10 + last_digit
            x = x // 10
        return (original == rev)