# Reverse Integer

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)
        value = 0
        while x > 0:
            rem = x % 10
            value = value * 10 + rem
            x //= 10
        value *= sign
        if value < -(2**31) or value > (2**31) - 1:
            return 0
        return value
