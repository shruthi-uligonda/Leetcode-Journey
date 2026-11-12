# Subarray Product less than K 

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        left = count = right = 0
        product = 1
        if k <= 1:
            return 0
        while right < len(nums):
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1
            count += right - left + 1
            right += 1
        return count
        
