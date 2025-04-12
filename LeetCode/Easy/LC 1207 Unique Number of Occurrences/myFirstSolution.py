def uniqueOccurrences(arr: list[int]) -> bool:
    occ = {}
    for num in arr:
        occ[num] = occ.get(num, 0) +1
    counts = [v for v in occ.values()]
    return len(counts) == len(set(counts))

print(uniqueOccurrences(arr = [1,2,2,1,1,3]))   #T
print(uniqueOccurrences(arr = [-3,0,1,-3,1,1,1,-3,10,0]))   #T
print(uniqueOccurrences(arr = [1,2]))   #F