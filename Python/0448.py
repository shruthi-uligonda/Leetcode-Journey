# Find All Numbers Disappeared in an Array

class Solution(object):
    def findDisappearedNumbers(self, nums):
        seen = [0] * (len(nums) + 1)
        for i in nums:
            seen[i] = 1
        res = []
        for i in range(1, len(nums) + 1):
            if seen[i] == 0:
                res.append(i)
        return res
