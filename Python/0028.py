# LeetCode 0028 - Find the Index of the First Occurrence in a String

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        '''n, m = len(haystack), len(needle)
        for s1 in range(n - m + 1):
            if haystack[s1:s1+m] == needle[:]:
                return s1
        return -1'''
        
        return haystack.find(needle)

