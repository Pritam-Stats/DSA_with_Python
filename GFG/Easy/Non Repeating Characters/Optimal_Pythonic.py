def nonRepeatingChar(s):
    #code here
    freq = {}   #O(N)
    for ch in s:    #O(N)
        freq[ch] = freq.get(ch, 0)+1
        
    for k,v in freq.items():
        if v == 1:
            return k
            
    return -1

print(nonRepeatingChar(s= "geeksforgeeks")) #f
print(nonRepeatingChar(s= "racecar")) #e
print(nonRepeatingChar(s= "aabbccc")) #-1
