# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if root==None:
            return 0

        self.pairs = 0
        self.dfs(root, distance)
        return self.pairs

    def dfs(self, root: TreeNode, distance:int) -> Dict[int, int]:
        if not root:
            return {}
        elif not root.left and not root.right:
            return {1:1}

        leftDist = self.dfs(root.left, distance)
        rightDist = self.dfs(root.right, distance)

        for lk in leftDist:
            for rk in rightDist:
                if lk+rk<=distance:
                    self.pairs+=leftDist[lk]*rightDist[rk]

        combined = defaultdict(int)
        for lk in leftDist:
            if lk+1 < distance:
                combined[lk+1] += leftDist[lk]

        for rk in rightDist:
            if rk+1 < distance:
                combined[rk+1] += rightDist[rk]
        
        return combined
