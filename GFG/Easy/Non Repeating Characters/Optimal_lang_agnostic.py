def nonRepeatingChar(s):
    #code here
    freq = [0]*26

    for ch in s:
        freq[ord(ch) - ord('a')] += 1

    for ch in s:
        if freq[ord(ch) - ord('a')] == 1:
            return ch
        
    return '$'

print(nonRepeatingChar(s= "geeksforgeeks")) #f
print(nonRepeatingChar(s= "racecar")) #e
print(nonRepeatingChar(s= "aabbccc")) #-1

# TC - O(n)