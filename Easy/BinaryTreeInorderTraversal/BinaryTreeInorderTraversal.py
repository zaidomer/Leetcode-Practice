# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ## VAlID NON-RECURSIVE SOLUTION
        stack = deque()
        result = []
        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right

        return result



        
        ## VALID RECUSRIVE SOLUTION
        # if root is None:
        #     return []

        # result = []

        # def inorder(node: TreeNode, result:List[int]):
        #     if node.left:
        #         inorder(node.left, result)
        #     result.append(node.val)
        #     if node.right:
        #         inorder(node.right, result)

        # inorder(root, result)
        # return result
