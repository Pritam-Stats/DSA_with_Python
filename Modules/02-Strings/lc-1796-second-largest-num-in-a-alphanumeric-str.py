https://leetcode.com/problems/second-largest-digit-in-a-string/description/

class Solution:
    def secondHighest(self, s: str) -> int:
        nums = set()
        for ch in s:
            if '0' <= ch <= '9':
                nums.add(int(ch))
        if len(nums) <= 1:
            return -1
        
        mx = float("-inf")
        smx = float("-inf")
        for x in nums:
            if x>mx:
                smx = mx
                mx = x
            elif smx < x < mx:
                smx = x
        
        return smx if smx != float("-inf") else -1


        