# https://leetcode.com/problems/binary-tree-coloring-game/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        ## VALID BFS
        # regions=defaultdict(int)
        # q = deque([(root, 0)])
        # while q:
        #     node, reg = q.popleft()
        #     left = reg if node.val!=x else 1
        #     right = reg if node.val!=x else 2
        #     regions[reg] += 1 if node.val!=x else 0

        #     if node.left:
        #         q.append((node.left, left))
        #     if node.right:
        #         q.append((node.right, right))

        # return regions[0]>n//2 or regions[1]>n//2 or regions[2]>n//2









        ## VALID DFS
        regions = [0,0]

        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            if node.val==x:
                regions[0] = left
                regions[1] = right

            return left+right+1

        dfs(root)
        return regions[0]>n//2 or regions[1]>n//2 or (n-(1+regions[0]+regions[1]))>n//2
