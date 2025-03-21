def generate_sandglass(n):
    """
    Function to return a sandglass pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the sandglass.
    
    Returns:
    list: A list of strings where each string represents a row of the sandglass pattern.
    
    
    Example:

    Input: 3
    Output: ['*****', ' *** ', '  *  ', ' *** ', '*****']

    Input: 4
    Output: ['*******', ' ***** ', '  ***  ', '   *   ', '  ***  ', ' ***** ', '*******']
    """
    # Your code here
    l = []
    for i in range(2*n -1, 1, -2):
        l.append(( "*" * i).center(2*n -1))
    for j in range(1, 2*n,2):
        l.append(( "*" * j).center(2*n -1))

    return l

result = generate_sandglass(3)
print(result)

# WITHOUT THE LIST - PRINTING THE PATTERN ONLY

n = int(input("Enter the Integer: "))
width = 2 * n - 1

# Print the top half of the sandglass
for i in range(width, 1, -2):
    print(("*" * i).center(width))

# Print the bottom half of the sandglass
for j in range(1, width + 1, 2):
    print(("*" * j).center(width))
