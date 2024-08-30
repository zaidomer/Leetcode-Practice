# https://leetcode.com/problems/find-duplicate-subtrees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        order = defaultdict(int)
        res = []
        
        def dfs(node):
            hash = ""
            if node.left:
                hash += 'L'+dfs(node.left)
            if node.right:
                hash += 'R'+dfs(node.right)
            hash += 'V'+str(node.val)
            if order[hash]==1:
                res.append(node)
            order[hash]+=1
            return hash
        
        dfs(root)
        return res
