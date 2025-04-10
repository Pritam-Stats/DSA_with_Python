def minChar(s: str)-> int:
    
    def computeLPS(string):
        lps = [0] * len(string) #will store the lengths for each idx of s
        l = 0   #length of the longest found palindrome
        
        i = 1   #since lps[0] is always 0
        while i < len(string):
            if string[i] == string[l]:  #if two chars matches
                l += 1
                lps[i] = l
                i += 1
                
            else: #if don't match
                if l != 0:  #if there is already some prev matches and failed now
                    l = lps[l - 1]  #assign l to that prev length not back to 0
                    
                else:
                    lps[i] = 0
                    i += 1
                    
        return lps
        
    rev = s[::-1]
    combined = s + '$' + rev
    lps = computeLPS(combined)  #last digit of the array will be longest palindrome available
    
    return len(s) - lps[-1]

print(minChar(s= 'abc'))    #2
print(minChar(s= 'aacecaaaa'))    #2