# LeetCode 0283 - Move Zeroes

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in nums:
            if j != 0:
                nums[i] = j
                i += 1
        for k in range(i, len(nums)):
            nums[k] = 0
        return nums
            
        
