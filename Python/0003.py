# Longest Substring Without Repeating Characters

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        new_arr = set()
        count = 0
        left = 0
        right = 0
        while right < len(s):
            if s[right] not in new_arr:
                new_arr.add(s[right])
                count += max(count, right - left + 1)
                right += 1
            else:
                new_arr.remove(s[left])
                left += 1
        return count
