def toUpper():
    word = input().strip()
    ans = ""
    for l in word:
        if 'a' <= l <= 'z':
            l = chr(ord(l) - ord('a') + ord("A"))
        ans += l
    return ans

print(toUpper())
    

