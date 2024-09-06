# https://leetcode.com/problems/bulls-and-cows/

class Solution:
    #O(n) time and space
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secretSet = defaultdict(int)
        guessSet = defaultdict(int)

        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls+=1
            else:
                secretSet[secret[i]]+=1
                guessSet[guess[i]]+=1
        
        for ch in secretSet:
            cows+=min(secretSet[ch], guessSet[ch])
        
        return str(bulls)+"A"+str(cows)+"B"
