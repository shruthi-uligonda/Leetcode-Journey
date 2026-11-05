# House Robber

class Solution(object):
    def rob(self, nums):
        dp = []
        for i in range(len(nums) + 1):
            dp.insert(i, -1)
        return self.calculate(nums, dp, len(nums) - 1)
    def calculate(self, nums, dp, n):
        if n < 0:
            return 0

        if n == 0:
            return nums[0]

        if dp[n] != -1:
            return dp[n]
        dp[n] = max(self.calculate(nums, dp, n-1), (nums[n] + self.calculate(nums, dp, n - 2)))
        return dp[n]
