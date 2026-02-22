def count_word_frequency(sentence: str) -> dict:
    word_dict = {}
    words = sentence.split()    # list of words

    for word in words:
        word_dict[word] = word_dict.get(word, 0) + 1

    return word_dict


    

print(count_word_frequency(sentence= "hello world hello"))