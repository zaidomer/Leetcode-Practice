# https://leetcode.com/problems/binary-tree-postorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #METHOD 1: Recursion
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.traverse(root, result)
        return result
        
    def traverse(self, root: Optional[TreeNode], arr:List[int]) -> None:
        if not root:
            return
        if root.left:
            self.traverse(root.left, arr)
        if root.right:
            self.traverse(root.right, arr)
        
        arr.append(root.val)