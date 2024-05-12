# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        # result = ""
        # arr = s.split()
        # for i in range(len(arr)-1,-1,-1):
        #     result += (arr[i])
        #     if i > 0:
        #         result += " "

        # return result

        result = ""
        nextWord = ""
        
        for i in range(0,len(s)):
            if not s[i].isalnum() and len(nextWord)>0:
                result = nextWord+' '+result
                print(result)
                nextWord=""
            elif s[i].isalnum():
                # print(s[i])
                nextWord += s[i]

        if len(nextWord)>0:
            result = nextWord+' '+result
            

        return result[:-1]