# https://leetcode.com/problems/subtree-of-another-tree/

# class Solution:
#     def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
#         if subRoot == None :
#             return True

#         if root == None :
#             return False

#         if self.same(root , subRoot):
#             return True
#         return self.isSubtree(root.left , subRoot) or self.isSubtree(root.right , subRoot)            

#     def same(self , root , subRoot):
#         if root == None and subRoot == None :
#             return True

#         if root and subRoot and root.val == subRoot.val:
#             return self.same(root.right , subRoot.right) and self.same(root.left , subRoot.left)  

#         return False



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSame(node:Optional[TreeNode], subNode:Optional[TreeNode]) -> bool:
            if node is None and subNode is None:
                return True
            elif (node is None or subNode is None) or (node.val!=subNode.val):
                return False
            
            return isSame(node.left, subNode.left) and isSame(node.right, subNode.right)

        if subRoot is None:
            return True
        elif root is None:
            return False
        elif isSame(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)