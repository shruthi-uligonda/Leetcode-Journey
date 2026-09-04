# 709 - Binary Search

class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        if target == nums[0]:
            return 0
        while (left <= right):
            mid = ( left + right ) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            elif target == nums[mid]:
                return mid
        return -1
        
