# https://leetcode.com/problems/longest-string-chain/

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # longestChain = 0
        # cache = {}

        # def differByOne(word1, word2):
        #     if len(word2)-len(word1)!=1:
        #         return False
        #     i = 0
        #     j = 0
        #     oneDiff = False
        #     while i<len(word1) and j<len(word2):
        #         if word1[i]!=word2[j]:
        #             if oneDiff:
        #                 return False
        #             j+=1
        #             oneDiff=True
        #         else:
        #             i+=1
        #             j+=1
        #     return True

        # def dfs(word):
        #     if word in cache:
        #         return cache[word]
        #     res = 1
        #     for nei in graph[word]:
        #         res = max(res, 1+dfs(nei))
        #     cache[word] = res
        #     return res

        # graph = defaultdict(list)
        # for i in range(0, len(words)):
        #     for j in range(0, len(words)):
        #         if i!=j and differByOne(words[i], words[j]):
        #             graph[words[i]].append(words[j])

        # for word in words:
        #     longestChain = max(longestChain, dfs(word))

        # return longestChain

        










        # dp = defaultdict(int)
        # res = 1
        # words.sort(key=lambda w: len(w))
        
        # for w in words:
        #     for i in range(len(w)):
        #         dp[w] = max(dp[w], dp[w[:i] + w[i+1:]] + 1)
        #         res = max(res, dp[w])

        # return res










        dp = {}
        res = 1
        words.sort(key=lambda w: -len(w))
        wordIndex = {}
        longest = 1

        for i in range(len(words)):
            wordIndex[words[i]] = i

        def dfs(i):
            nonlocal longest
            if i in dp:
                return dp[i]
            word = words[i]
            res = 1
            for j in range(len(word)):
                newWord = word[0:j] + word[j+1:]
                if newWord in wordIndex:
                    res = max(res, 1+dfs(wordIndex[newWord]))
            dp[i] = res
            longest = max(longest, res)
            return res

        for i in range(len(words)):
            dfs(i)
        return longest
        