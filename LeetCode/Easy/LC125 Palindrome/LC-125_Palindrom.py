def isPalindrome(s: str) -> bool:
    #we have to remove all alpha numeric character
    # we can use regex substitute
    import re
    cleaned_s = re.sub(pattern = r'[^a-zA-Z0-9]', repl = "", string = s).lower()
    
    return True if cleaned_s == cleaned_s[::-1] else False


########################## Approach 2 : Two Pointer ############################
def isPalindrome2(s: str) -> bool:
    # two pointer approach
    n = len(s)
    left, right = 0, n-1

    while left < right :
        # skips the non alpha numerics and update the pointers
        # below we will check for false. imagine we already assumed that it's Palindrome
        while left<right and not s[left].isalnum():
            left += 1
        while left<right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower(): #return False if any char doesn't match
            return False
        # update to check the next pair of chars
        left += 1
        right -=1

    return True

print(isPalindrome(s = "race a car"))
print(isPalindrome2(s = "a2_a"))