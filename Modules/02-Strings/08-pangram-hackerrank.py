'''  
    Author: Pritam
''' 
'''  
Problem: pangram https://www.hackerrank.com/challenges/pangrams/problem
Technique: basic
Intuition: len of the set
Mistake: input handling
Time: 
Space: 
''' 
import sys
from sys import stdin
input = stdin.readline


def pangrams():
    # Write your code here
    s = input().split()
    s = "".join(s)

    s = s.lower()


    if len(set(s)) == 26:
        print("pangram")
    else:
        print("not pangram")
pangrams()