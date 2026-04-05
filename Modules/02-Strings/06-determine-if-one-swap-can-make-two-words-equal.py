'''  
    Author: Pritam
''' 
'''  
Problem: Given two words they are close if we can get another word by swapping or replacing related prob: LC 1657
Technique: two ways: counter dict; or find differences
Intuition: 
Mistake: 
Time: 
Space: 
'''

def isClose(s1, s2):
    if len(s1) != len(s2):
        return False
    
    diffCharFromS1, diffCharFromS2 = None, None
    diff = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            ## we found a mismatch char
            if diff == 0:
                diffCharFromS1 = s1[i]
                diffCharFromS2 = s2[i]
            else:
                if diffCharFromS1 != s2[i] or diffCharFromS2 != s1[i]:
                    # means another new difference 
                    return False
            diff += 1
        
            if diff > 2:
                return False
    if diff == 1:
        return False
    return True
