# 209 - Minimum Size Subarray Sum

class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = right = s = 0
        min_length = len(nums) + 1
        while (right < len(nums)):
            s += nums[right]
            while s >= target:
                length = right - left + 1
                min_length = length if length < min_length else min_length

                s -= nums[left]
                left += 1
            right += 1
        if min_length == len(nums) + 1:
            return 0
        return min_length
