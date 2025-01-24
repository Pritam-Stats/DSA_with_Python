def generate_square(n):
    """
    Function to return a square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the square.
    """
    # Your code here
    l = [] #empty list, we will append
    for i in range(n):
        l.append(n * "*")
    
    return l

result = generate_square(3)

#USING LIST COMPREHENSION

def generate_sq(n):
    if n <= 0:      #edge case
        return []
    return [n * "*" for _ in range(n)]

result2 = generate_sq(5)

print(result2)