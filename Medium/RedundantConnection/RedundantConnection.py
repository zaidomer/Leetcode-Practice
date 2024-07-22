# https://leetcode.com/problems/redundant-connection/

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # graph = defaultdict(list)

        # for a,b in edges:
        #     graph[a].append(b)
        #     graph[b].append(a)

        # def dfs(node:int, r1:int, r2:int, prev:int, visit:Set[int]):
        #     if node in visit:
        #         return False

        #     visit.add(node)
        #     for con in graph[node]:
        #         if con==prev or (node==r1 and con==r2) or (node==r2 and con==r1):
        #             continue
        #         elif not dfs(con, r1, r2, node, visit):
        #             return False
        #     visit.remove(node)
        #     return True


        # for j in range(len(edges)-1,-1,-1):
        #     a = edges[j][0]
        #     b = edges[j][1]

        #     if dfs(a, a, b, -1, set()) and dfs(b, a, b, -1, set()):
        #         return edges[j]

        # return []

        parent = [i for i in range(0, len(edges)+1)]
        rank = [1 for _ in range(0, len(edges)+1)]

        def find(node:int):
            par = parent[node]
            while par!=parent[par]:
                parent[par]=parent[parent[par]]
                par = parent[par]

            return par

        def union(n1:int, n2:int):
            p1 = find(n1)
            p2 = find(n2)

            if p1==p2:
                return False

            if rank[p1]>rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1]=p2
                rank[p2] += rank[p1]
            return True

        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]

