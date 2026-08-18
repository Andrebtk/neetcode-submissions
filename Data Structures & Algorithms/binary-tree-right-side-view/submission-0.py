# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        q = deque()
        res = []
        if root:
            q.append(root)

        while len(q) > 0:
            lenQ = len(q)
            for i in range(lenQ):

                node = q.popleft()

                if i == (lenQ - 1):
                    res.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
                