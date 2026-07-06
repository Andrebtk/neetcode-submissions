# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is not None:
            depL = 0
            depR = 0
            
            if root.left is not None:
                depL = self.maxDepth(root.left)
            
            if root.right is not None:
                depR = self.maxDepth(root.right)
            
            return 1 + max(depL, depR)
        return 0