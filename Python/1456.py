# 1456 - Maximum Number of Vowels in a Substring of a Given Length

class Solution(object):
    def maxVowels(self, s, k):
        left = right = count = 0
        vowels = 'aeiou'
        max_count = 0
        while(right < len(s)):
            if s[right] in vowels:
                count += 1
            if right - left + 1 == k:
                max_count = max(max_count, count)
                if s[left] in vowels:
                    count -= 1 
                left += 1
            right += 1
        return max_count
