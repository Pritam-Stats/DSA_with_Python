'''
    Author: Pritam
'''
'''
    Problem: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
'''



class Solution:

    def maxVowelsOptimal(self, s: str, k: int) -> int:
        '''  
            Technique: simple sliding window
            Intuition: only use sliding window traditional approach
            Mistake: 
            Time: O(n)
            Space: O(1)
        '''
        n = len(s)
        vowel = {'a', 'e', 'i', 'o', 'u'}
        # simple sliding window problem
        count = 0
        for i in range(k):
            # first window
            if s[i] in vowel:
                count += 1
        maxCount = count
        if maxCount == k:
            return k

        for i in range(k, n):
            if s[i] in vowel:
                count += 1  # add new
            if s[i-k] in vowel:
                count -= 1  # remove the old

            maxCount = max(maxCount, count)
            if maxCount == k:
                return k
        return maxCount



#-------------------------------------------------------------------------------

    def maxVowelsBruteForce(self, s: str, k: int) -> int:
        '''
            Technique: Sliding window but brute force
            Intuition: 
            Mistake: tle, was checking and counting vowel for every single window
            Time: O(n*k)
            Space: O(1)

            1<= n, k <= 10**5
        '''
        n = len(s)
        vowel = {'a', 'e', 'i', 'o', 'u'}

        def countVowel(st: list):
            count = 0
            for l in st:
                if l in vowel:
                    count += 1
            return count
        maxCount = 0
        for i in range(n-k+1):
            st = i
            end = i+k
            maxCount = max(maxCount, countVowel(s[st:end]))
        return maxCount

    ##-------------------------------------------------------------------------------


    def maxVowelsBetter(self, s: str, k: int) -> int:
        '''  
            Technique: Sliding window, contribution, prefix sum
            Intuition: convert the str to a binary array 1 if vowel
            Mistake: in range; window len 2 means 0, 1 not 0-2
            Time: O(n)
            Space: O(n)
        '''
        n = len(s)
        vowel = {'a', 'e', 'i', 'o', 'u'}
        s_binary_contribution_arr = [0]*n
        i = 0
        for letter in s:
            if letter in vowel:
                s_binary_contribution_arr[i] = 1
            else:
                s_binary_contribution_arr[i] = 0
            i += 1
        ps = [0]*n
        curSum = 0
        for i in range(n):
            curSum += s_binary_contribution_arr[i]
            ps[i] = curSum
        # sliding window
        maxCount = 0
        for l in range(n-k+1):
            r = l + k-1
            if l == 0:
                windowSum = ps[r]
            else:
                windowSum = ps[r] - ps[l-1]
            maxCount = max(maxCount, windowSum)
        return maxCount


s = Solution()
print(s.maxVowelsBruteForce("aeiou", 2))    #2
print(s.maxVowelsBetter("abciiidef", 3))    #3
print(s.maxVowelsOptimal("weallloveyou", 7))    #4
