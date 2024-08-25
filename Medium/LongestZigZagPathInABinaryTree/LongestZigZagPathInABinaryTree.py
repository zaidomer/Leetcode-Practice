# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node, prevLeft, currLen):
            nonlocal res
            if node is None:
                return
            elif currLen>res:
                res = currLen

            if prevLeft:
                dfs(node.right, False, currLen+1)
                dfs(node.left, True, 1)
            else:
                dfs(node.left, True, currLen+1)
                dfs(node.right, False, 1)
            
        dfs(root, False, 0)
        return res
