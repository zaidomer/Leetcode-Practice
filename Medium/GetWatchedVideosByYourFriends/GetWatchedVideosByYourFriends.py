# https://leetcode.com/problems/get-watched-videos-by-your-friends/

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        #Time: O(V+E+MlogM), Space: O(V+M) where M is number of vidoes
        visit = {id}
        freq = defaultdict(int)
        dist = 0
        q = deque([id])

        while q and dist<level:
            for i in range(len(q)):
                node = q.popleft()
                for nei in friends[node]:
                    if nei not in visit:
                        q.append(nei)
                        visit.add(nei)
            dist+=1
        
        while q:
            person = q.popleft()
            for vid in watchedVideos[person]:
                freq[vid]+=1

        return sorted([vid for vid in freq.keys()], key=lambda m: (freq[m], m))
