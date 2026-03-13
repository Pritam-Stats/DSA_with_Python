def generate_hollow_right_angled_triangle(n):
    """
    Function to return a hollow right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    
    Example:

    Input: 4
    Output: ['*', '**', '* *', '****']
    
    Input: 5
    Output: ['*', '**', '* *', '*  *', '*****']
    """
    # Your code here
    l = []
    for i in range(1, n+1):
        if i == 1:
            row = "*"
        elif i == n:
            row = "*" * n
        else:
            if (i + 1) == 2:
                row = "**"
            else:
                row = "*" + " " * (i - 2) + "*"
        l.append(row)


    return l
result = generate_hollow_right_angled_triangle(5)
print(result)