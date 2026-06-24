# LeetCode 0224 - Basic Calculator

class Solution(object):
    def calculate(self, s):
        stack = []
        result , num, sign = 0, 0, 1

        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)

            elif char in ['+','-']:
                result += sign * num
                num = 0
                sign = 1 if char == '+' else -1

            elif char =='(':
                stack.append(result)
                stack.append(sign)
                result, sign = 0, 1

            elif char ==')':
                result += sign * num
                num = 0
                result *= stack.pop()
                result += stack.pop()

        return result + sign * num
