# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.traverseCompare(root.left, root.right)

    def traverseCompare(self, leftRoot: Optional[TreeNode], rightRoot: Optional[TreeNode]) -> bool:
        if leftRoot is None and rightRoot is None:
            return True
        elif leftRoot is None or rightRoot is None:
            return False
        elif leftRoot.val == rightRoot.val:
            return self.traverseCompare(leftRoot.left, rightRoot.right) and self.traverseCompare(rightRoot.left, leftRoot.right)
        else:
            return False

