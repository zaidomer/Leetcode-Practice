# https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        a = set()
        b = set()
        n = len(graph)

        def dfs(node, isA):
            curr = a if isA else b
            opp = b if isA else a

            if node in curr:
                return True
            elif node in opp:
                return False

            curr.add(node)
            for nei in graph[node]:
                if not dfs(nei, not isA):
                    return False
            return True

        for i in range(n):
            if i not in a and i not in b and not dfs(i, True):
                return False
        return True
        