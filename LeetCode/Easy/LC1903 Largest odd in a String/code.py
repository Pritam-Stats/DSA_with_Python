class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        for i in range(n-1, -1, -1):
            if (int(num[i]) % 2) == 1:
                return num[ : i+1]
        return ""
    
sol = Solution()
print(sol.largestOddNumber("52") == '5')
print(sol.largestOddNumber("4206") == '')
print(sol.largestOddNumber("527") == '527')
print(sol.largestOddNumber("53457") == '53457')