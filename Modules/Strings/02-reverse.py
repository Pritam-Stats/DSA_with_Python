def revChar():
    word = list(input().strip())
    n = len(word)
    st, end = 0, n-1
    while st < end:
        #swap st and end
        word[st], word[end] = word[end], word[st]
        st += 1
        end -= 1
    return "".join(word)

print(revChar())