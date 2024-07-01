# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        result = []
        graph = defaultdict(list)
        ancestors = [set() for _ in range(n)]
        incomingNodes = [0 for _ in range(n)]

        for start,end in edges:
            graph[start].append(end)
            ancestors[end].add(start)
            incomingNodes[end]+=1

        #when there are no incoming nodes for the current node considered, it 
        #means all of that node's ancestors have been added
        q = deque()
        for node in range(n):
            if incomingNodes[node]==0:
                q.append(node)

        #pop the nodes which have no ancestors (or who's ancestors have already been added)
        #Can then begin to go down the graph and consider that node's children (the other nodes it points to)
        while q:
            node = q.popleft()
            for childNode in graph[node]:
                ancestors[childNode].update(ancestors[node])
                incomingNodes[childNode]-=1
                if incomingNodes[childNode]==0:
                    q.append(childNode)

        #sort and append all ancestors
        for i in range(0, len(ancestors)):
            result.append(sorted(ancestors[i]))
        return result
