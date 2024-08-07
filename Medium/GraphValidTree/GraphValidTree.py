# https://leetcode.com/problems/graph-valid-tree/description/
# https://neetcode.io/problems/valid-tree

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visit = set()
        graph = defaultdict(list)
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in graph[node]:
                if nei!=prev and not dfs(nei, node):
                    return False
            return True

        if not dfs(0, -1) or len(visit)<n:
            return False
        return True
    