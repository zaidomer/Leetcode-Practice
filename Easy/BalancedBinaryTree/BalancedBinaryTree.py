# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # def findDepth(node:Optional[TreeNode]) -> int:
        #     if node is None:
        #         return 0
        #     return 1 + max(findDepth(node.left), findDepth(node.right))

        # if root is None:
        #     return True

        # dl=findDepth(root.left)
        # dr=findDepth(root.right)
        # if abs(dl-dr)>1:
        #     return False
        # else:
        #     return self.isBalanced(root.left) and self.isBalanced(root.right)





        def dfs(node:Optional[TreeNode]):
            if node is None:
                return (True, 0)

            left=dfs(node.left)
            right=dfs(node.right)
            isBalanced = left[0] and right[0] and abs(left[1]-right[1])<=1

            return (isBalanced, 1+max(left[1], right[1]))

        return dfs(root)[0]

