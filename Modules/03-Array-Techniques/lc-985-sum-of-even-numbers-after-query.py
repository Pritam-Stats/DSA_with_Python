'''  
    Author: Pritam
''' 
'''  
Problem: 
Technique: contribution
Intuition: 
Mistake: brute force
Time: O(n*q)
Space: 
'''     
## TLE



def sumEvenAfterQueriesOptimal(nums: list[int], queries: list[list[int]]) -> list[int]:
    ans = []

    evenSum = sum(x for x in nums if x % 2 == 0)  # init

    for v, i in queries:
         if (nums[i] % 2) == 0:
             evenSum -= nums[i]  # remove old
         nums[i] += v
         if (nums[i]) % 2 == 0:
             evenSum += nums[i]  # add new
         ans.append(evenSum)
    return ans

def sumEvenAfterQueriesBF(nums: list[int], queries: list[list[int]]) -> list[int]:
    '''
        Author: Pritam
    '''
    ans = []
    def addeven(arr):
        ans = 0
        for x in arr:
            if x % 2 == 0:
                ans += x
        return ans
    for v, i in queries:
        nums[i] = nums[i] + v
        ans.append(addeven(nums))
    return ans



arr = [1, 2, 3, 4]
q = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
print(sumEvenAfterQueriesBF(arr, q))  # [8,6,2,4]
arr = [1, 2, 3, 4]
q = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
print(sumEvenAfterQueriesOptimal(arr, q))  # [8,6,2,4]