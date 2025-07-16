class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        count_in_ans = 0
        for ch in s:
            if ch == '(':
                if count_in_ans > 0:
                    #not outermost
                    ans.append(ch)
                count_in_ans += 1
            else:
                count_in_ans -= 1
                if count_in_ans > 0:
                    ans.append(ch)
        return ''.join(ans)


sol = Solution()

print(sol.removeOuterParentheses("(()())(())") == "()()()")
print(sol.removeOuterParentheses("(()())(())(()(()))") == "()()()()(())")
print(sol.removeOuterParentheses("()()") == "")