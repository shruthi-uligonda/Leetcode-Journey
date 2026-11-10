# Maximum Product Subarray

class Solution(object):
    def maxProduct(self, nums):
        maximum = minimum = result = nums[0]
        i = 1
        for i in range(1, len(nums)):
            a = maximum * nums[i]
            b = minimum * nums[i]

            maximum = max(nums[i], a, b)
            minimum = min(nums[i], a, b)

            result = max(result, maximum)
        return result
