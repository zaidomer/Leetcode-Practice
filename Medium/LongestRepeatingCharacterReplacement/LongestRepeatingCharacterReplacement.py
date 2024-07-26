# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # window = defaultdict(int)
        # result = 0
        # left = 0

        # for right in range(len(s)):
        #     window[s[right]]+=1

        #     while right-left+1-max(window.values())>k and left<right:
        #         window[s[left]]-=1
        #         left+=1
            
        #     result = max(result, (right-left+1))

        # return result






        window = defaultdict(int)
        result = 0
        left = 0
        mostFreq = 0

        #AAAABBAAA    k=1

        for right in range(len(s)):
            window[s[right]]+=1
            mostFreq = max(mostFreq,window[s[right]])

            while right-left+1-mostFreq>k and left<right:
                window[s[left]]-=1
                left+=1
            
            result = max(result, (right-left+1))

        return result
