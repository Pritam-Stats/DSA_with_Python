def evenlyDivides(n):
    # code here
    counter = 0
    for d in str(n):
        if int(d) == 0:     #edge case
            pass
        elif (n % int(d)) == 0:
            counter += 1
        else:
            pass
        
    return counter

result = evenlyDivides(200)
print(result)
