'''
You are given an integer n. Your task is to return a pyramid pattern of '*' where each side has n rows, represented as a list of strings. The pyramid is centered, with 1 star in the first row, 3 stars in the second row, and so on, increasing by 2 stars per row until the base row has 2n - 1 stars.
Input:
A single integer n, where 1 <= n <= 100.

Output:
A list of strings where each string contains stars ('*') centered, forming a pyramid shape. Each row has an increasing number of stars, with appropriate spaces for centering.

Example:

Input: 3
Output: ['  *  ', ' *** ', '*****']

Input: 5
Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********']
'''

def generate_pyramid(n):
    l = [ ]
    for i in range(1, 2*n, 2):
        l.append(("*" * i).center(2*n - 1))     #new learning: center() method of string class

    return l

result = generate_pyramid(5)
print(result)

#INVERTED PYRAMID

def generate_inverted_pyramid(n):
    """
    Function to return an inverted pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the inverted pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the inverted pyramid.
    """
    # Your code here
    l = [ ]
    
    for i in range(2*n -1, 0, -2):
        l.append(("*" * i).center(2*n - 1))
        
    return l
    
result = generate_inverted_pyramid(3)
print(result)