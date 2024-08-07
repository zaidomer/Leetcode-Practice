# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node:Optional[TreeNode], minVal:int, maxVal:int) -> bool:
            if node is None:
                return True
            elif (node.val<=minVal) or (node.val>=maxVal):
                return False
            else:
                return dfs(node.left, minVal, node.val) and dfs(node.right, node.val, maxVal) 

        return dfs(root, float("-inf"), float("inf"))
