# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node:Optional[TreeNode], depth:int) -> None:
            if not node:
                return

            if (depth+1)<=len(result):
                result[depth] = max(result[depth], node.val)
            else:
                result.append(node.val)

            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root, 0)
        return result
