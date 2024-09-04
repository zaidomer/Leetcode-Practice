# https://leetcode.com/problems/loud-and-rich/?envType=problem-list-v2&envId=graph

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        N = len(quiet)
        graph = defaultdict(list)
        for rich,poor in richer:
            graph[poor].append(rich)
        res = []
        cache = {}

        def dfs(person):
            if person in cache:
                return cache[person]
            
            quietestPerson = person
            for nei in graph[person]:
                temp = dfs(nei)
                if quiet[temp]<quiet[quietestPerson]:
                    quietestPerson = temp

            cache[person] = quietestPerson
            return quietestPerson

        for i in range(N):
            res.append(dfs(i))
        return res
