'''
Diamond Pattern

Problem Description:
You are given an integer n. Your task is to return a diamond pattern of '*' with n rows for the upper part (the widest row will have 2n - 1 stars), and the lower part is the mirrored version of the upper part. Each row should be centered with appropriate spaces.


Input:
A single integer n, where 1 <= n <= 100.


Output:
A list of strings where each string represents a row in the diamond pattern.

Example:

Input: 3
Output: ['  *  ', ' *** ', '*****', ' *** ', '  *  ']

Input: 5
Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']

'''


def diamond(n: int) -> list:
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows for the upper part of the diamond.
    
    Returns:
    list: A list of strings where each string represents a row of the diamond.
    """
    l = []
    for i in range(1, 2 * n, 2):
        l.append(("*" * i).center(2*n - 1))
    for j in range(2*n - 3, 0, -2):       #for the end part
        l.append(("*" * j).center(2*n - 1))
    
    return l

result = diamond(5)
print(result)