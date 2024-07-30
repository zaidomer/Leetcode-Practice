# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # VALID DFS SOLUTION
        # if not root:
        #     return []

        # result = []

        # def dfs(node:Optional[TreeNode], level:int, result:List[int]) -> None:
        #     if node is None:
        #         return

        #     if level>=len(result):
        #         result.append([])
        #     result[level].append(node.val)

        #     dfs(node.left, level+1, result)
        #     dfs(node.right, level+1, result)

        # dfs(root, 0, result)
        # return result



        #BFS SOLUTION
        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            curr = []
            for i in range(len(q)):
                node = q.popleft()
                curr.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            result.append(curr)

        return result
