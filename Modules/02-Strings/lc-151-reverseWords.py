'''  
    Author: Pritam
''' 
'''  
Problem: LC 151 https://leetcode.com/problems/reverse-words-in-a-string/description/
Technique: 
Intuition: 
Mistake: "  hello world   " handling multiple spaces
Time: O(n)
Space: O(n)
''' 


def reverseWords(s: str) -> str:
    s = s.split(" ")
    # return s
    ans = []
    n = len(s)
    for i in range(n-1, -1, -1):
        if s[i] != "":
            ans.append(s[i])
    return " ".join(ans)


print(reverseWords(s="  hello world  "))
