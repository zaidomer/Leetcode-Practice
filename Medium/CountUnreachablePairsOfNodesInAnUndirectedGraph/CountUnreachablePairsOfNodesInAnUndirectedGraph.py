# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        #VALID DFS APPROACH
        # graph = defaultdict(list)
        # for a,b in edges:
        #     graph[a].append(b)
        #     graph[b].append(a)
        # visit = set()

        # def dfs(node):
        #     if node in visit:
        #         return 0
        #     visit.add(node)
        #     res = 1
        #     for nei in graph[node]:
        #         res += dfs(nei)
        #     return res

        # product = []
        # for i in range(n):
        #     if i not in visit:
        #         product.append(dfs(i))

        # if len(product)==1:
        #     return 0
        # res = 0
        # for i in range(len(product)):
        #     res += product[i]*(n-product[i])
        #     n-=product[i]
        # return res











        # VALID UNION FIND APPROACH
        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def find(node):
            par = parent[node]
            while par!=parent[par]:
                parent[par] = parent[parent[par]]
                par = parent[par]
            return par

        def uunion(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1==p2:
                return False
            if rank[p1]>rank[p2]:
                parent[p2] = p1
                rank[p1]+=rank[p2]
            else:
                parent[p1] = p2
                rank[p2]+=rank[p1]
            return True

        for a,b in edges:
            uunion(a,b)


        for i in range(n):
            parent[i] = find(i)
        
        count = Counter(parent)
        res = 0
        for val in count.values():
            res += val*(n-val)
            n-=val
        return res
