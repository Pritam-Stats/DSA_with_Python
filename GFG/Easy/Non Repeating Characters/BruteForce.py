def nonRepeatingChar(s):
    #code here
    for i in range(len(s)):
        found_duplicates = False    #init

        for j in range(len(s)): #for each i there is a new j
            if i != j and s[i] == s[j]: #to found matches
                found_duplicates = True
                break

        if not found_duplicates:
            return s[i]


    return -1

print(nonRepeatingChar(s= "geeksforgeeks")) #f
print(nonRepeatingChar(s= "racecar")) #e
print(nonRepeatingChar(s= "aabbccc")) #-1

# TC - O(n**2)