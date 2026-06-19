# LeetCode 0242 - Valid Anagram 

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        d = {}
        for char in s:
            d[char] = s.count(char)
        for char in t:
            if char not in d:
                return False
            d[char] -= 1
        return all(value == 0 for value in d.values())
            
        
