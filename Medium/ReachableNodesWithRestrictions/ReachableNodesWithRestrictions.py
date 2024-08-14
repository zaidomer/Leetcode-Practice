# https://leetcode.com/problems/reachable-nodes-with-restrictions/

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        visit = set(restricted)
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            res=0
            visit.add(node)
            for nei in graph[node]:
                if nei not in visit:
                    res+=dfs(nei)
            return 1+res
        
        return dfs(0)
