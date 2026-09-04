# 643 - Maximum Average Subarray I

class Solution(object):
    def findMaxAverage(self, nums, k):
        left = right = s = 0
        maximum = float('-inf')
        while (right < len(nums)):
            s += nums[right]
            if right - left + 1 == k:
                maximum = max(maximum, s)
                s -= nums[left]
                left += 1
            right += 1
        return float(maximum) / k
