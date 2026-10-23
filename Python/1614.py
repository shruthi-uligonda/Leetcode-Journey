# Maximum Nesting Depth of the Parentheses

class Solution(object):
    def maxDepth(self, s):
        stack = []
        ans = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == ')':
                stack.pop()
            ans = max(ans,len(stack))
        return ans
