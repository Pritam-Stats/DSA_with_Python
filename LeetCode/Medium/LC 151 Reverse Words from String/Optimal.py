def reverseWords(s: str) -> str:
    # words = s.strip().split()
    # return ' '.join(reversed(words))
    words = []
    i = len(s) - 1
    while i >= 0:
        #hadnling spaces
        while i >= 0 and s[i] == ' ':
            i -= 1
        if i < 0:
            break
        
        # detecting the words
        j = i
        while j>=0 and s[j] != ' ':
            j -= 1  #j wil be stopped at the index which will have a space
            #to get the range of the word or non spaced
        words.append(s[j+1 : i+1])
        i = j-1 #now change the i
    return ' '.join(words)


print(reverseWords(s = "the sky is blue"))  #"blue is sky the"
print(reverseWords(s = "  hello world  "))  #"world hello"
print(reverseWords(s = "a good   example")) #"example good a"


# this is the DSA Approach without any builtin function