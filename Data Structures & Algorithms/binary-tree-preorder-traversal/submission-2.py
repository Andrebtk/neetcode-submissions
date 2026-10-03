# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [(False, root)]


        while stack:
            visited, node = stack.pop()

            if not node:
                continue
            
            if visited:
                res.append(node.val)
            else:
                stack.append((False, node.right))
                stack.append((False, node.left))
                stack.append((True, node))
        

        return res