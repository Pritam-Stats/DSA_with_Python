'''  
    Author: Pritam
''' 
'''  
Problem: anagram
Technique: count array
Intuition: prepare a count array with the first word; index can be built using ord values; this can also be done using dict and get
Mistake: count array preparation
Time: O(n)
Space: O(n)
''' 
def isAnagram():
    s1 = list(input().lower().strip())
    s2 = list(input().lower().strip())

    if len(s1) != len(s2):
        print("They are NOT anagrams")
        return False
    
    count = [0] *26
    a = ord("a")

    for ch in s1:
        count[ord(ch) - a] += 1
    
    for ch in s2:
        if count[ord(ch) - a] > 0:
            count[ord(ch) - a] -= 1
        else:
            print("They are NOT anagrams")
            return False
    print("They are anagrams")
    return True

isAnagram()



    