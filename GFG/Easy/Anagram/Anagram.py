
def areAnagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    freq1 = {}  #dict
    freq2 = {}
    

    for c, d in zip(s1, s2):
        freq1[c] = freq1.get(c, 0) +1  #default count is 0 or increase by 1
        freq2[d] = freq2.get(d, 0) +1  #default count is 0 or increase by 1

    return (freq1 == freq2)

print(areAnagrams(s1 = "geeks", s2 = "kseeg"))  #True
print(areAnagrams(s1="listen", s2="silent"))   # True
print(areAnagrams(s1="hello", s2="bello"))     # False
print(areAnagrams(s1="aabbcc", s2="baccab"))   # True
print(areAnagrams(s1="abc", s2="abcd"))        # False
