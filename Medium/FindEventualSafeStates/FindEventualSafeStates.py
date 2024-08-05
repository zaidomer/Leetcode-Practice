# https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = {}

        def dfs(node):
            if node in safe:
                return safe[node]
            
            safe[node]=False
            for nei in graph[node]:
                if not dfs(nei):
                    return safe[node]
            
            safe[node]=True
            return safe[node]


        res=[]
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)

        return res
