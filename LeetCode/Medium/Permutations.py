def permutations(arr: list[int]) -> list[list[int]]:
    # recursion -> backtracking
    n = len(arr)
    ans = []
    def getPerms(idx, ans):
        """Helper Function

        Args:
            idx (_type_): _description_
            ans (_type_): _description_
        """
        if idx == n -1: # base case
            ans.append(arr[:])  #will append a list
            return
        
        for i in range(idx, n): #for each index of the og arr
            arr[idx], arr[i] = arr[i], arr[idx]

            getPerms(idx+1, ans)
            arr[idx], arr[i] = arr[i], arr[idx]

    getPerms(0, ans)

    return ans


print(permutations(arr= [1,2,3]))