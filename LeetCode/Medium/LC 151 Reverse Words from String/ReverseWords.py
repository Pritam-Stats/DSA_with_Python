def reverseWords(s: str) -> str:

    # words = s.strip().split()
    # return ' '.join(reversed(words))

# Pythonic Solution and Efficient too TC O(N)

    # below is the manual solution and less efficient as well
    words = []
    n = len(s)
    word = ""
    for ch in s:
        if ch != " ":
            word += ch
        elif word:
            words.append(word)
            word = ""
    if word:
        words.append(word)
    #reverse the words list
    words = words[::-1]
    return ' '.join(words)

print(reverseWords(s = "the sky is blue"))  #"blue is sky the"
print(reverseWords(s = "  hello world  "))  #"world hello"
print(reverseWords(s = "a good   example")) #"example good a"