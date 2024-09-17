# https://leetcode.com/problems/shortest-path-with-alternating-colors/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        #Time: O(V+E), Space: O(V+E) (not O(V) space here because had to build the graph)
        red = defaultdict(list)
        blue = defaultdict(list)
        redVisit = set()
        blueVisit = set()
        count = 0
        res = [-1 for _ in range(n)]
        q = deque([(0, True)])

        for src,dst in redEdges:
            red[src].append(dst)
        
        for src,dst in blueEdges:
            blue[src].append(dst)

        def traverse(node, isRed):
            graph = red if isRed else blue
            visit = redVisit if isRed else blueVisit
            for nei in graph[node]:
                if nei not in visit:
                    q.append((nei, not isRed))
                    visit.add(nei)

        while q:
            for i in range(len(q)):
                node, exploreRed = q.popleft()
                if res[node]==-1:
                    res[node]=count
                
                if node==0 or exploreRed:
                    traverse(node, True)
                    red[node] = []
                if node==0 or not exploreRed:
                    traverse(node, False)
                    blue[node] = []
            count+=1

        return res
