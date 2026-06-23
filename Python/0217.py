# LeetCode 0217 - Contains Duplicate

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # First Way
        nums.sort() 
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

        # Second Way
        count = set([])
        for i in nums:
            if i in count:
                return True
            else:
                count.add(i)
        return False
