# def pushZerosToEnd(arr):
# 	# code here
# 	n = len(arr)
# 	# new_ls = []
# 	# count = 0
# 	for i in range(n -1):
# 		if arr[i] == 0:
# 			arr.remove(arr[i])
# 			arr.insert(n-1,0)
# 	return arr

# https://www.geeksforgeeks.org/batch/gfg-160-problems/track/arrays-gfg-160/problem/move-all-zeroes-to-end-of-array0751

# Normal Brute Force Approach

def pushZerosToEnd(arr: list) -> list:
    temp_arr = []
    for n in arr:
        if n != 0:
            temp_arr.append(n)
    
    n0 = len(arr) - len(temp_arr)
    temp_arr += [0]*n0

    return temp_arr

print(pushZerosToEnd(arr= [3,5,0,0,4]))

# print([0]*5)