def isSubsequence(s: str, t: str) -> bool:
    if len(s) == len(t) and s == t:
        return True
    
    i = 0
    for ch in t:
        if i < len(s) and s[i] == ch:
            i += 1
    return i == len(s)

print(isSubsequence(s = "abc", t = "ahbgdc"))   #T
print(isSubsequence(s = "axc", t = "ahbgdc"))   #F
