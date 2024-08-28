# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
# https://neetcode.io/problems/count-connected-components

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        def find(node):
            p = parent[node]
            while p!=parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def uunion(n1, n2):
            p1 = find(n1)
            p2 = find(n2)
            if p1==p2:
                return 0
            parent[p1] = p2
            return 1

        res = n
        for n1,n2 in edges:
            res -= uunion(n1,n2)

        return res
