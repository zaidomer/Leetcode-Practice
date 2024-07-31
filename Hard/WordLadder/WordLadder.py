# https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # graph = defaultdict(list)
        # if beginWord not in set(wordList):
        #     wordList.append(beginWord)

        # def differByOne(word1:str, word2:str):
        #     differ = 0
        #     for i in range(len(word1)):
        #         if word1[i]!=word2[i]:
        #             differ+=1
        #             if differ>=2:
        #                 return False
        #     return True
        

        # for i in range(len(wordList)):
        #     w1 = wordList[i]
        #     for j in range(i+1, len(wordList)):
        #         w2 = wordList[j]
        #         if differByOne(w1, w2):
        #             graph[w1].append(w2)
        #             graph[w2].append(w1)

        # count=1
        # q = deque([beginWord])
        # visit = set()
        # while q:
        #     count+=1
        #     for i in range(len(q)):
        #         curr = q.popleft()
        #         for word in graph[curr]:
        #             if word not in visit:
        #                 if word==endWord:
        #                     return count
        #                 q.append(word)
        #                 visit.add(word)

        # return 0 







        graph = defaultdict(list)
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        if beginWord not in wordSet:
            wordList.append(beginWord)
        

        for i in range(len(wordList)):
            word = wordList[i]
            for j in range(len(word)):
                pattern = word[:j] + '*' + word[j+1:]
                graph[pattern].append(word)

        count=1
        q = deque([beginWord])
        visit = set()
        while q:
            for i in range(len(q)):
                curr = q.popleft()
                if curr==endWord:
                    return count
                for j in range(len(curr)):
                    pattern = curr[:j] + '*' + curr[j+1:]
                    for word in graph[pattern]:
                        if word not in visit:
                            q.append(word)
                            visit.add(word)
            count+=1

        return 0 
