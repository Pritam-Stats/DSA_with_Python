'''
#PROBLEM STATEMENT

You are given an integer n. Your task is to return the first n rows of Floyd’s Triangle, represented as a list of strings. Floyd's Triangle is a triangular array of natural numbers where the first row contains 1, the second row contains 2 and 3, the third row contains 4, 5, and 6, and so on.
'''

'''
Input:
A single integer n, where 1 <= n <= 100.

Output:
A list of strings where each string represents a row in Floyd's Triangle.

Example:

Input: 5
Output: ['1', '2 3', '4 5 6', '7 8 9 10', '11 12 13 14 15']

Input: 3
Output: ['1', '2 3', '4 5 6']
'''

def floyds_triangle(n : int)-> list :
    l = []
    num = 1     #for each row
    for i in range(1, n + 1):
        rows = ''       #for storing the rows | a list can also be used
        for j in range(i):
            rows += str(num) + " "
            num += 1

        l.append(rows.strip())
    return l


result = floyds_triangle(3)
print(result)

#2ND METHOD

def floyds_triangle2(n: int) -> list:
    l = []
    num = 1
    for i in range(1, n + 1):
        row = []  # List to store numbers for the current row
        for j in range(i):
            row.append(str(num))  # Add the number to the row list
            num += 1
        l.append(" ".join(row))  # Join numbers with spaces and append
    return l

result2 = floyds_triangle(3)
print(result2)


def floydTri(n):
    num = 1
    for i in range(n+1):
        for _ in range(i):
            print(num, end=" ")
            num += 1
        print()

floydTri(5)