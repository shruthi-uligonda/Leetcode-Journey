# LeetCode 0020 -  Valid Parentheses

class Solution(object):
    def isValid(self, s):
        stack = []
        matching = {")":"(","]":"[","}":"{"}
        for char in s:
            if char in matching:
                top_element = stack.pop() if len(stack) > 0 else '_'
                if matching[char] != top_element:
                    return False
            else:
                stack.append(char) 
        return len(stack) == 0
        
        
