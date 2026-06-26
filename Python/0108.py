# LeetCode 0108 - Convert Sorted Array to Binary Search Tree

class Solution(object):
    def sortedArrayToBST(self, nums):
        def helper(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
        return helper(0, len(nums) - 1)
        
