# https://leetcode.com/problems/distribute-coins-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root, None)

    def traverse(self, root, parent):
        if root==None: 
            return 0
        moves=self.traverse(root.left, root)+self.traverse(root.right, root)
        x=root.val-1
        if parent!=None: 
            parent.val+=x
            moves+=abs(x)
        return moves


        