# https://leetcode.com/problems/binary-tree-pruning/

# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #Time: O(n), Space: O(n)
        if root is None:
            return None

        leftDfs = self.pruneTree(root.left)
        rightDfs = self.pruneTree(root.right)

        if root.val==0 and rightDfs is None and leftDfs is None:
            return None
        else:
            root.left = leftDfs
            root.right = rightDfs
        
        return root
