# https://leetcode.com/problems/online-election/

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.votes = defaultdict(int)
        self.winnerByTime = []
    
        currWinner = self.persons[0]
        for i in range(len(self.times)):
            self.votes[self.persons[i]]+=1
            if self.votes[self.persons[i]]>=self.votes[currWinner]:
                currWinner = self.persons[i]
            self.winnerByTime.append(currWinner)

    def q(self, t: int) -> int:
        l = 0
        r = len(self.times)-1
        winner = None
        
        while l<=r:
            mid = l + (r-l)//2
            if self.times[mid] == t:
                return self.winnerByTime[mid]
            elif self.times[mid]<t:
                winner = self.winnerByTime[mid]
                l = mid+1
            else:
                r = mid-1
        return winner
