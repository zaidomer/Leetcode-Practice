# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 


class Solution:
    
    def goodNodes(self, root: TreeNode) -> int:
        ##VALID BFS APPROACH
        # count = 0
        # q = deque([(root, float("-inf"))])
        
        # while q:
        #     for i in range(len(q)):
        #         node, currMax = q.popleft()
        #         if node.val>=currMax:
        #             count+=1
        #             currMax = node.val
        #         if node.left:
        #             q.append((node.left, currMax))
        #         if node.right:
        #             q.append((node.right, currMax))

        # return count






        ## VALID DFS APPROACH
        count=0
        
        def dfs(node:Optional[TreeNode], currMax:int):
            nonlocal count
            if node is None:
                return 
        
            if node.val >= currMax:
                count+=1
                currMax = node.val

            dfs(node.left, currMax)
            dfs(node.right, currMax)

        dfs(root, float("-inf"))
        return count