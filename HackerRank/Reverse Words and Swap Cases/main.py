def reverse_words_swap_cases(sentence: str) -> str:
    words = sentence.split()[::-1]
    swapped = [word.swapcase() for word in words]

    return ' '.join(swapped)


if __name__ == "__main__":
    print(reverse_words_swap_cases(sentence= "AweSOME is cODING"))  #Coding IS aWEsome.
    print(reverse_words_swap_cases(sentence='rUNS dOG'))    #Dog Runs