# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a,b,weight in roads:
            graph[a].append((b, weight))
            graph[b].append((a, weight))
        visit = set()

        def dfs(node):
            if node in visit:
                return
            nonlocal res
            visit.add(node)
            for nei,weight in graph[node]:
                res = min(res, weight)
                dfs(nei)

        res = float("inf")
        dfs(1)
        return res
