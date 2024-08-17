# https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = deque([(root,1)])
        res = 0

        while q:
            res = max(res, 1+q[-1][1]-q[0][1])
            for i in range(len(q)):
                node, count = q.popleft()

                if node.right:
                    q.append((node.right, count*2))
                if node.left:
                    q.append((node.left, count*2+1))

        return res
        