def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    # Your code here
    l = []
    if n <= 0:
        return []
    elif n < 3:
        return [n * "*" for _ in range (n)]
    else:
        l.append(n * "*")       #first row all *s
        for _ in range(n - 2):         #middle rows 2 stars and n-2 spaces in middle so need n - 2 iterations
            l.append("*" + (" " * (n - 2)) + "*")    
        l.append(n* "*")        #last row all *s
    
        return l
        
result = generate_hollow_square(1)
print(result)
    
    
    
    