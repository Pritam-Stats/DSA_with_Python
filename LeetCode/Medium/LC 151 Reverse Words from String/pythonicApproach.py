def reverseWords(s: str) -> str:

    words = s.strip().split()
    return ' '.join(reversed(words))

print(reverseWords(s = "the sky is blue"))  #"blue is sky the"
print(reverseWords(s = "  hello world  "))  #"world hello"
print(reverseWords(s = "a good   example")) #"example good a"
#though this is using builtin function but this is also efficient with O(N) TC SC
