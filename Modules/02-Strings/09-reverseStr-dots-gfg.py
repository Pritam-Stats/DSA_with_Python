'''  
    Author: Pritam
''' 
'''  
Problem: https://www.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1
Technique: traditional loop
Intuition: split
Mistake: how to handle multiple dots
Time: O(n)
Space: O(n)
''' 



def reverseWords(s):
    # code here
    s = s.split(".")
    # return s
    n = len(s)
    ans = []
    for i in range(n-1, -1, -1):
        if s[i] != "":
            ans.append(s[i])

    return ".".join(ans)

print(reverseWords(".geeks.for..geeks."))
