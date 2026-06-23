# LeetCode 0125 - Valid Palindrome

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        low = 0
        high = len(s) - 1
        while low < high:
            while low < high and not s[low].isalnum():
                low += 1
            while low < high and not s[high].isalnum():
                high -= 1
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True
