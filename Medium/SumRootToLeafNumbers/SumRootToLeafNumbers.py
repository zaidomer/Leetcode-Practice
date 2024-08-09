# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ## VALID BFS APPROACH
        # q = deque([(root, 0)])
        # total = 0

        # while q:
        #     node,currNum = q.popleft()
        #     currNum = currNum*10+node.val
        #     if node.left is None and node.right is None:
        #         total+=currNum
        #     else:
        #         if node.left:
        #             q.append((node.left, currNum))
        #         if node.right:
        #             q.append((node.right, currNum))
        # return total





        ## VALID DFS APPROACH
        if root is None:
            return 0

        def dfs(node, currNum):
            currNum = currNum*10+node.val
            if node.left is None and node.right is None:
                return currNum

            total = 0
            if node.left:
                total += dfs(node.left, currNum)
            if node.right:
                total += dfs(node.right, currNum)
            return total

        return dfs(root, 0)
        