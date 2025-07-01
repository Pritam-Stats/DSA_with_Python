def findMajority(arr):
    #Your Code goes here.
    # there will be atmost 2 candidates
    candidate1, candidate2 = None, None
    vote1, vote2 =0, 0
    n = len(arr)
    
    for num in arr:
        if candidate1 == num:
            vote1 += 1
            
        elif candidate2 == num:
            vote2 += 1
            
        elif vote1 == 0:
            candidate1 = num
            vote1 = 1
            
        elif vote2 == 0:
            candidate2 = num
            vote2 = 1
            
        else: #if votes are non 0 and candidates are assigned but didnt match then decrease vote
            
            vote1 -= 1
            vote2 -= 1

    count1, count2 = 0, 0
    for num in arr:
        count1 += (num == candidate1)
        count2 += (num == candidate2)
            # pythonic way to write if else and increase count

    

    return [candidate for candidate, count in [(candidate1, count1), (candidate2, count2)] if count > n //3]   
#list comprehension to return the list of candidates if count of each matches the requirement to be > n/3
    
print(findMajority(arr= [1,1,2]))