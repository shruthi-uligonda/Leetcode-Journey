# LeetCode 0033 - Search in Rotated Sorted Array

class Solution(object):
    def search(self, nums, target):
        # Type - 1
        '''if target in nums:
            return nums.index(target)
        else:
            return -1'''
        # Type - 2
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid 
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid] :
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1 
