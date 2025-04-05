def reverseVowels(s: str) -> str:
    # means vowels will move to the opp position
    n = len(s)
    vowels = ['a', 'e', 'i', 'o', 'u']
    present_vowels = []
    for ch in s:
        if ch.lower() in vowels:
            present_vowels.append(ch)
    #now we need to rev the vowels and add in the same idxs
    present_vowels = present_vowels[::-1]
    # p = len(present_vowels)
    # for i in range(p//2):
    #     present_vowels[i], present_vowels[p -i-1] = present_vowels[p-i-1], present_vowels[i]
    #reversed
    #now to replace
    s = list(s) #string is immutable so convert to list
    j = 0
    for i in range(n):
        if s[i].lower() in vowels:  #whenever a vowel gets detected
            s[i] = present_vowels[j]
            j += 1  #will remain less than p
    return ''.join(s) 

# SC TC O(N)
#Runtime ~ 23ms 
#Memory ~18MB
#leetcode

# Input:  "hello"       ➝ Output: "holle"
# Input:  "leetcode"    ➝ Output: "leotcede"
# Input:  "aA"          ➝ Output: "Aa"
