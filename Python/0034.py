# LeetCode 0034 - Find First and Last Position of Element in Sorted Array

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def bin_search(find_left):
            low , high = 0,len(nums) - 1
            boundary =- 1
            while low <= high:
                mid = (low +  high) //2
                if nums[mid] < target:
                    low = mid +1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    # Found Target
                    boundary = mid
                    if find_left:
                        high = mid - 1
                    else :
                        low = mid + 1

            return boundary 
        first_pos = bin_search(True)
        last_pos = bin_search(False)
        return [first_pos, last_pos]
