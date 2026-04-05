def longestPalindrome(s: str) -> str:
    #Approach - Expand Around Center
    n = len(s)
    if not s:
        return ""
    
    st, maxLen = 0, 1
    def expand_around_center(left: int, right: int) -> None:
        """This func updates the st and maxLen"""
        nonlocal st, maxLen
        while left >= 0 and right < n and s[left] == s[right]:
            currLen = right - left + 1
            if currLen > maxLen:
                maxLen = currLen
                st = left
            left -= 1
            right += 1

    for i in range(n):
        #for odd len
        expand_around_center(i, i)
        
        #for even
        expand_around_center(i, i+1)
    return s[st : st+maxLen]


        