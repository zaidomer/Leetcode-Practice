# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # groups = defaultdict(list)
        # for word in strs:
        #     groups[''.join(sorted(word))].append(word)
        # return groups.values()







        groups = defaultdict(list)
        for word in strs:
            count = [0 for _ in range(26)]
            for ch in word:
                count[ord(ch)-ord('a')]+=1
            groups[tuple(count)].append(word)
        return groups.values()
        