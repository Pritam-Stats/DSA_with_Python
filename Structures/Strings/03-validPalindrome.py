'''  
    Author: Pritam
''' 
'''  
Technique: Two pointer
Intuition: 
Mistake: 
Time: O(n)
Space: O(1)
''' 

def isPalindrome(word):
    word = list(word.strip())
    st, end = 0, len(word) - 1

    while st< end:
        if word[st] != word[end]:
            return False
        st += 1
        end -= 1
    return True

word = "apple"
print(isPalindrome(word))
word = "racecar"
print(isPalindrome(word))