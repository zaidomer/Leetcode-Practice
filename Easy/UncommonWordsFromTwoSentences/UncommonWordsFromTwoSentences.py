# https://leetcode.com/problems/uncommon-words-from-two-sentences/

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # Time: O(n), Space: O(n) where n is # words
        count = Counter((s1 + " " + s2).split(' '))
        res = []
        for word in count:
            if count[word]==1:
                res.append(word)
        return res
