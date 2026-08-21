# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        currSum = 0
        def dfs(node, targetSum):
            nonlocal currSum
            if node is None:
                return False
            
            currSum += node.val
            
            # A leaf
            if node.left is None and node.right is None:
                if currSum == targetSum:
                    return True
            
            # Other
            if dfs(node.left, targetSum):
                return True
            if dfs(node.right, targetSum):
                return True
            
            currSum -= node.val
            return False


        return dfs(root, targetSum)