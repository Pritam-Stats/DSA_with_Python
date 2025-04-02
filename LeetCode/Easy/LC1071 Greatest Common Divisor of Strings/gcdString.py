def gcdOfStrings(str1: str, str2: str) -> str:
    # from math import gcd
    
    if str1 + str2 != str2+str1:
        return ""
    
    def find_gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    gcdlength = find_gcd(len(str1), len(str2))
    
    
    return str1[:gcdlength]

print(gcdOfStrings(str1="ABCABC", str2="ABC"))
print(gcdOfStrings(str1="ABCAB", str2="ABC"))
print(gcdOfStrings(str1="ABAB", str2="AB"))
print(gcdOfStrings(str1="LEET", str2="CODE"))
