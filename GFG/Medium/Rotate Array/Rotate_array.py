# [1,2,3,4,5] -> [3,4,5,1,2] (rotated by 2 elem)
#consider the array as circular
# counter clock wise
#User function Template for python3

#Function to rotate an array by d elements in counter-clockwise direction. 
        #Your code here
def rotateArr(arr: list, d: int)-> list:
    n = len(arr)
    if d > n:
        d = d%n
    def reverse(arr: list, start: int, end:int)-> list:
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
            
    # first reverse the first d elements
    reverse(arr, 0, d -1)
    
    # reverse the rest n-d of ehe elements
    reverse(arr, d, n-1)
    
    # reverse the entire arr
    reverse(arr, 0, n-1)
            
            
        
    return arr
            









