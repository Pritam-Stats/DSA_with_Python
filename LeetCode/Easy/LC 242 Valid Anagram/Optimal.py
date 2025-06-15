def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1    #increasing the count by 1

    # for c in t:
    #     freq[c] = freq.get(c, 0) - 1    #default is zero but whenever we finding the same key we are decreasing by 1


    ## the following will also work in replace of the prev and its slightly better for the early exit
    for c in t:
        if c in s:
            freq[c] -= 1
        else:
            return False
    #so if anagram we are supposed to left with all values as 0

    for v in freq.values():
        if v != 0:
            return False
    
    return True

print(isAnagram(s="geeks", t="kseeg"))     # True
print(isAnagram(s="listen", t="silent"))   # True
print(isAnagram(s="hello", t="bello"))     # False
print(isAnagram(s="aabbcc", t="baccab"))   # True
print(isAnagram(s="abc", t="abcd"))        # False
