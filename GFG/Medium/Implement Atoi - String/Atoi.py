def myAtoi(s):
    # Code here
    res = 0
    sign = 1
    n = len(s)
    idx = 0
    
    while idx < n and s[idx] == " ":    #blank space
        idx += 1
        
    if idx < n and (s[idx] == "-" or s[idx] == "+"):
        if s[idx] == "-":
            sign = -1
        idx += 1
        
    while idx < n and ('0' <= s[idx] <= '9'):   # or could have used s[idx].isdigit()
        res = (res*10) + int(s[idx])    #ord(s[idx] - ord['0']) could have been used instead of int()
        
        if res > (2**31 -1):
            return (2**31 -1) if sign == 1 else -2**31
            
        idx += 1
        
    return sign*res


print(myAtoi("   -42")         )    #➝ -42
print(myAtoi("   +123")        )    #➝ 123
print(myAtoi("4193 with words"))    #➝ 4193
print(myAtoi("words and 987")  )    #➝ 0
print(myAtoi("-91283472332")   )    #➝ -2147483648 (clamped to lower bound)
print(myAtoi("21474836460")    )    #➝ 2147483647 (clamped to upper bound)
