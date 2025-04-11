def areRotations(s1: str, s2 : str) -> bool:
    if len(s1) != len(s2):
        return False
    return s2 in s1+s1  #this is all if it says both are equal length

print(areRotations(s1="abcd", s2 = "cdab")) #T After 2 right rotations, s1 will become equal to s2
print(areRotations(s1 = "abcd", s2 = "acbd")) #F - Strings are not rotations of each other.
print(areRotations(s1 = "aab", s2 = "aba")) #T - After 1 left rotation, s1 will become equal to s2.