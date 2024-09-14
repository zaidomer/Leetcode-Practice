# https://leetcode.com/problems/recover-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        #Time: O(n), Space: O(n)
        nodes = []
        i=0
        def dfs(node, setVal):
            nonlocal i
            if node.left:
                dfs(node.left, setVal)
            if not setVal:
                nodes.append(node.val)
            else:
                node.val = nodes[i]
                i+=1
            if node.right:
                dfs(node.right, setVal)
        dfs(root, False)
        nodes.sort()
        dfs(root, True)
        return root
