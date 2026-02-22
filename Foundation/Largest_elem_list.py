'''
Largest Element in a List
Find the Largest Element in a List

Write a Python function that finds and returns the largest element in a given list of integers.

Parameters:

numbers (List of integers): The input list containing integers.

Returns:

An integer representing the largest element in the input list.

Example:

Input: numbers = [3, 8, 2, 10, 5]
Output: 10

Input: numbers = [-5, -10, -2, -1, -7]
Output: -1
'''

# def largest_element(num:list) -> int:     #we can use this but then no point of solving this
#     return max(num)

def largest_element(num:list) -> int:
    if not num:         #Handle empty list
        return None
    
    largest = num[0]            #AN INITIALIZATION WITH THE FIRST ELEMENT

    for i in range(1, len(num)):
        if num[i] > largest:
            largest = num[i]

    return largest

print(largest_element([9, 5, 30]))