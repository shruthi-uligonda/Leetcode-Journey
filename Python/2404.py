# LeetCode 2404 - Most Frequency Even Element

class Solution(object):
    def mostFrequentEven(self, nums):
        freq = {}
        """
        :type nums: List[int]
        :rtype: int
        """
        for num in nums:
            if num % 2 == 0:
                freq[num] = freq.get(num,0) + 1
        if not freq:
            return -1
        arr = sorted(freq.items(),
                key = lambda x: (-x[1],x[0]))
        return arr[0][0]        
