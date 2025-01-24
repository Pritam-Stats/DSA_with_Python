def prefixCount(words: list[str], pref: str) -> int:
    counter = 0
    for word in words:
        if word.startswith(pref):
            counter += 1
    return counter

print(prefixCount(["apple", "app", "apricot", "banana", "apocalypse"], "ap"))
