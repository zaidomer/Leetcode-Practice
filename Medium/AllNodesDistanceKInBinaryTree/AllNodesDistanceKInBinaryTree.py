# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        res = []
        graph = defaultdict(list)
        q = deque([root])
        while q:
            node = q.popleft()
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                q.append(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                q.append(node.right)
        
        def dfs(node, dist):
            if node in visit:
                return
            elif dist==0:
                res.append(node)
                return
            visit.add(node)
            for nei in graph[node]:
                print(nei)
                dfs(nei, dist-1)

        visit = set()
        dfs(target.val, k)
        return res
        