'''  
    Author: Pritam
''' 
'''  
Problem: https://www.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1
Technique: Sliding window with map to access O(1) ops
Intuition: normal sliding approach, 
Mistake: tle at the last test case - so solution is correct but needs optimization
Time: O(nk)
Space: O(n) #worst case when k == 1
''' 
class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        if k == 1:
            return arr
        
        ans = []
        n = len(arr)
        
        maxS = 0
        freq = {}
        
        for i in range(k):
            freq[arr[i]] = freq.get(arr[i], 0) + 1  #O(k)   #first window

        maxS = max(freq)

        ans.append(maxS) #first window sum
        
        for i in range(k, n):
            freq[arr[i]] = freq.get(arr[i], 0) + 1
            
            freq[arr[i-k]] -= 1
            
            if freq[arr[i-k]] == 0:
                del freq[arr[i-k]]

            maxS = max(freq)
            ans.append(maxS)
            
        return ans
    

    ## so let's code this now. 
    ## my mic is having some problem so no mic, i am explaining here

    def maxOfSubarraysOptimal(self, arr, k):
        # code here
        n = len(arr)

        ans = []

        currMax = 0 

        ## first window
        currMax = max(arr[:k])  #arr[:k] -> first k elements of arr. O(k) tc

        ans.append(currMax)

        ## now
        for i in range(k, n):
            if arr[i] > currMax:
                currMax = arr[i]        

            else:
                if currMax == arr[i-k]:
                    currMax = max(arr[i-k + 1 : i+1]) 

            #O(1)

            ans.append(currMax)

        return ans
    
s = Solution()
print(s.maxOfSubarrays([1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3))

print(s.maxOfSubarraysOptimal([1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3))

'''
Problem: https://leetcode.com/problems/sliding-window-maximum/description/
Mistake: The above solution is tle as well
needs perfect O(n)
'''

