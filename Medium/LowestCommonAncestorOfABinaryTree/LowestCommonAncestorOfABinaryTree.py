# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # def dfs(node:'TreeNode', target:'TreeNode', path):
        #     if not node:
        #         return False
        #     elif node==target or dfs(node.left, target, path) or dfs(node.right, target, path):
        #         path.append(node)
        #         return True

        #     return False

        # pPath = []
        # qPath = []
        # dfs(root, p, pPath)
        # dfs(root, q, qPath)

        # res = None
        # for i in range(0, min(len(pPath), len(qPath))):
        #     if pPath[len(pPath)-1-i]!=qPath[len(qPath)-1-i]:
        #         return res
        #     else:
        #         res = pPath[len(pPath)-1-i]

        # return res




        if not root or root==p or root==q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if not left:
            return right
        elif not right:
            return left
        else:
            return root

