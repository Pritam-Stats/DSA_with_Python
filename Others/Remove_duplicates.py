'''
Remove Duplicate in a List
Remove Duplicates from a List

You are given a list of integers. Write a Python program that removes any duplicate elements from the list and returns a new list with only unique elements. The order of elements in the list should be maintained.

Parameters:

lst (List of integers): The list of integers from which duplicates should be removed.

Returns:

A list of integers where all duplicates have been removed, preserving the original order.

Example:

Input: lst = [1, 2, 2, 3, 4, 4, 5]
Output: [1, 2, 3, 4, 5]

Input: lst = [4, 5, 5, 4, 6, 7]
Output: [4, 5, 6, 7]


Note :- Please don't use set or inbuilt functions. Try to use brute force logic.
'''

def rm_duplicates(lst:list) -> list:
    if not lst:
        return None
    
    unique_list = []
    for num in lst:
        if num not in unique_list:
            unique_list.append(num)
    return unique_list

print(rm_duplicates([1, 2, 2, 3, 4, 4, 5]))


###############################################################

'''
CHECK UNIQUENESS - RETURN TRUE IF THE LIST IS UNIQUE OTHERWISE FALSE
'''

def check_unique(lst):
    # Your code goes here
    if not lst:
        return None
    
    unique_list = []
    for num in lst:
        if num not in unique_list:
            unique_list.append(num)
    
    if unique_list == lst:
        return True
    else:
        return False
print(check_unique(lst = [1, 2, 3, 4, 5]))