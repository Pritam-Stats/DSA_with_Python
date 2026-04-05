# LC503
def next_greater(nums:list)->list:
    n = len(nums)
    ans = [-1]*n
    stack = []

    #so we can run twice
    for i in range(2*n -1, -1, -1):
        j = i%n
        while stack and stack[-1] <= nums[j]:
            stack.pop()
        if stack:
            ans[j] = stack[-1]

        stack.append(nums[j])

    return ans

#catch is it's circular

print(next_greater(nums= [2, 3, 4, 6, 1]))  # ans = [3, 4, 6, -1, 2]