# https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)

        def dfs(node, curr):
            curr.append(node)
            if node==n-1:
                res.append(curr)
                return

            for nei in graph[node]:
                dfs(nei, curr[:])

        dfs(0, [])
        return res
