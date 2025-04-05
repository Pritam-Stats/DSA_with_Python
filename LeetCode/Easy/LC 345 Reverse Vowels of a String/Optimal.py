def reverseVowels(s: str) -> str:
    vowels = set('aeiouAEIOU')
    left, right = 0, len(s)-1
    s = list(s)
    while left < right:
        while left < right and s[left] not in vowels:
            left += 1 
        while left < right and s[right] not in vowels:
            right -= 1 
        
        #else just swap the vowels
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)

#more efficient
# Runtime 11ms