# LeetCode 0110 - Balanced Binary Tree

class Solution(object):
    def isBalanced(self, root):
        # Bottom - Up DFS
        def height_check(node):
            if not node:
                return 0
            left_height = height_check(node.left)
            if left_height == -1:
                return -1
            right_height = height_check(node.right)
            if right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:    # abs = absolute
                return -1
            return max(left_height, right_height) + 1
        return height_check(root) != -1
