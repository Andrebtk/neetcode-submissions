# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [(False, root)]

        res = []


        while stack:
            visited, node = stack.pop()

            if not node:
                continue
            
            if visited:
                res.append(node.val)
            else:
                
                stack.append((False, node.right))
                stack.append((True, node))
                stack.append((False, node.left))
        

        return res