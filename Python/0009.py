# Palindrome Number

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        temp = x
        value = 0
        while temp > 0:
            rem = temp % 10
            value = value * 10 + rem
            temp //= 10
        return value == x
        
