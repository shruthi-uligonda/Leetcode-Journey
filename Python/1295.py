# Find Numbers with Even Number of Digits

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_count = 0
        for i in range(len(nums)):
            digit_count = 0
            temp = nums[i]
            while temp > 0:
                rem = temp % 10
                digit_count += 1
                temp //= 10
            if digit_count % 2 == 0:
                total_count += 1
        return total_count
