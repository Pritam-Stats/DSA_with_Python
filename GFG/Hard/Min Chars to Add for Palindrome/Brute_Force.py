def minChar(s: str) -> int:
    #Write your code here
    
    #helper funtion to check the palindrome
    def isPalindrome(s, L, R):  #left=0 and right = n-1
        while L < R:
            # palindrome will have the same start and end
            if s[L] != s[R]:
                return False
                
            L += 1
            R -= 1
        return True
            
    
    n = len(s)
    idx = n-1   #R
    count = 0
    
    while idx >= 0 and not isPalindrome(s, L = 0, R = idx): #here it becomes O(n**2) TC
        idx -= 1    #need to update the idx first then count
        count += 1
        
    return count
    
    #the logic = len(s) - len(longest palindrome present)

print(minChar(s= 'abc'))    #2
print(minChar(s= 'aacecaaaa'))    #2