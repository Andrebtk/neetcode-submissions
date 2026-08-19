# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()

        res = []

        if root is not None:
            q.append(root)


        while len(q) > 0:
            tmpL = []
            for index in range(len(q)):
                node = q.popleft()
                
                tmpL.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
                
            res.append(tmpL)

        return res