# https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ## DFS Solution

        result = []
        def dfs(root: Optional[TreeNode], depth:int) -> None:
            if not root:
                return
            elif len(result)<(depth+1):
                result.append(None)
        
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
            result[depth]=root.val
            
        dfs(root,0)
        return result



        ## BFS SOLUTION possible (neetocode)

        # result = []
        # q = deque()
        # q.append(root)

        # while q:
        #     rightSide = None
        #     qLen = len(q)

        #     for i in range(qLen):
        #         node = q.popleft()
        #         if node:
        #             rightSide = node
        #             q.append(node.left)
        #             q.append(node.right)

        #     if rightSide:
        #         result.append(rightSide.val)

        # return result