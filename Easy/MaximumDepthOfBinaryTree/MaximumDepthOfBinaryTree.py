# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ## VALID BFS SOLUTION
        # if root is None:
        #     return 0

        # result = 0
        # q = deque([root])
        # while q:
        #     result+=1
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        # return result        





        ## VALID ITERATIVE DFS SOLUTION
        # if not root:
        #     return 0

        # stack = deque([(root, 1)])
        # result = 1

        # while stack:
        #     node,depth = stack.pop()
        #     if node:
        #         result = max(result, depth)
        #         stack.append((node.left, depth+1))
        #         stack.append((node.right, depth+1))
        # return result




        
        ## VALID DFS SOLUTION
        # if root is None:
        #     return 0

        # def dfs(node:Optional[TreeNode], depth:int) -> int:
        #     if not node:
        #         return depth
        #     elif node.left is None and node.right is None:
        #         return depth

        #     return max(dfs(node.left, depth+1), dfs(node.right, depth+1))

        # return dfs(root, 1)





        ## CONCISE DFS SOLUTION
        if root is None:
            return 0

        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))