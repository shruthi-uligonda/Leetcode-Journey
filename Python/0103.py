# Binary Tree Zigzag Level Order Traversal

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        q = []
        q.append(root)
        while q:
            s = len(q)
            level = []
            for i in range(s):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)   
            if len(result) % 2 == 1:
                level.reverse()
            result.append(level) 
        return result     
