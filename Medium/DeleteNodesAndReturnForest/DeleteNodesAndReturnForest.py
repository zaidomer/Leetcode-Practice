# https://leetcode.com/problems/delete-nodes-and-return-forest/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
#         deleteSet = set(to_delete)
#         result = {root}
#         self.traverse(root, deleteSet, result)
#         return result

#     def traverse(self, root:Optional[TreeNode], to_delete:Set[int], result:Set[Optional[TreeNode]]):
#         if not root:
#             return 

#         if root.val in to_delete and root in result:
#             result.remove(root)
#             if root.left:
#                 result.add(root.left)
#             if root.right:
#                 result.add(root.right)

#         if root.left and root.left.val in to_delete:
#             self.traverse(root.left, to_delete, result)
#             if root.left.left:
#                 result.add(root.left.left)
#             if root.left.right:
#                 result.add(root.left.right)
#             root.left = None
#         if root.right and root.right.val in to_delete:
#             self.traverse(root.right, to_delete, result)
#             if root.right.left:
#                 result.add(root.right.left)
#             if root.right.right:
#                 result.add(root.right.right)
#             root.right = None

#         self.traverse(root.left, to_delete, result)
#         self.traverse(root.right, to_delete, result)
            
        
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        self.deleteSet = set(to_delete)
        self.result = {root}
        self.traverse(root)
        return list(self.result)

    def traverse(self, root:Optional[TreeNode]):
        if not root:
            return

        returnNode = root
        if root.val in self.deleteSet:
            returnNode = None
            self.result.discard(root)

            if root.left:
                self.result.add(root.left)
            if root.right:
                self.result.add(root.right)

        root.left = self.traverse(root.left)
        root.right = self.traverse(root.right)
        return returnNode
            