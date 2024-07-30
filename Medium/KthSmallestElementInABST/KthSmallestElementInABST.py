# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ## VALID NON-RECUSIVE APPROACH
        # if root is None:
        #     return -1

        # stack = deque()
        # node = root
        # curr=0

        # while node or stack:
        #     while node:
        #         stack.append(node)
        #         node = node.left
        #     node = stack.pop()
        #     curr+=1
        #     if curr==k:
        #         return node.val
        #     node = node.right

        # return 0






        ## VALID RECUSION APPROACH
        curr=0
        res=-1

        def inorder(node:Optional[TreeNode]):
            nonlocal curr
            nonlocal res

            if node.left:
                inorder(node.left)
            curr+=1
            if curr==k:
                res=node.val
                return
            if node.right:
                inorder(node.right)

        inorder(root)
        return res
        