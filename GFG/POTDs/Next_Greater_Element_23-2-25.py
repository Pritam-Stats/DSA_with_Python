'''
Problem - 

Given an array arr[ ] of integers, the task is to find the next greater element for each element of the array in order of their appearance in the array. Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.
'''

##NOT DONE NEED STACK CONCEPTS

def nextLargerElement(arr):
    n = len(arr)
    stack = []
    result = [-1] * n  # Initialize result with -1

    # Traverse from right to left
    for i in range(n - 1, -1, -1):
        # Pop smaller elements from the stack
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        # If stack is not empty, the top is the NGE
        if stack:
            result[i] = stack[-1]

        # Push current element to stack
        stack.append(arr[i])

    return result

# Example
print(nextLargerElement([1, 3, 2, 4]))  # Output: [3, 4, 4, -1]












# def nextLargerElement(arr):
#     # code here
#     pointer = 0
#     l = []
#     while pointer < (len(arr)):
#         if arr[pointer] == max(arr):
#             l.append(-1)
#         elif arr[pointer] > arr[pointer + 1]:
#             l.append(arr[pointer])
#         else:
#             l.append(arr[pointer + 1])
        
#         pointer += 1
    
#     return l

# print(nextLargerElement(arr = [1,3,2,4]))