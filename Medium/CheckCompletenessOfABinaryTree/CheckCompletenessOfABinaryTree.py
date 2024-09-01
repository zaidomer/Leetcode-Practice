# https://leetcode.com/problems/check-completeness-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, 1)])
        prev = 0
        while q:
            node, i = q.popleft()
            if i!=prev+1:
                return False
            if node.left:
                q.append((node.left, i*2))
            if node.right:
                q.append((node.right, i*2+1))
            prev = i

        return True
