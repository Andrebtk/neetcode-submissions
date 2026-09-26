# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root


        while True:
            val = curr.val

            if val > p.val and val > q.val:
                curr = curr.left
            elif val < p.val and val < q.val:
                curr = curr.right
            else:
                return curr