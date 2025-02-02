def generate_right_angled_triangle(n):
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    
    Example:

    Input: 4
    Output: ['   *', '  **', ' ***', '****']

    Input: 3
    Output: ['  *', ' **', '***']
    """
    # Your code here
    l = [ ((" "* (n-i)) + "*"* i) for i in range (1, n+1) ]
    
    return l

result = generate_right_angled_triangle(4)
print(result)