# https://leetcode.com/problems/generate-parentheses/

class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         result = []
        
#         def compute(currOpen:int, currClosed:int, resStr:str):
#             if len(resStr)==n*2:
#                 result.append(resStr)
#                 return

#             if currOpen<n:
#                 compute(currOpen+1, currClosed, resStr+"(")
#             if currClosed<currOpen:
#                 compute(currOpen, currClosed+1, resStr+")")    
        
#         compute(1,0,"(")
#         return result






    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = deque()
        
        def compute(currOpen:int, currClosed:int):
            if currOpen==currClosed==n:
                result.append("".join(stack))
                return

            if currOpen<n:
                stack.append("(")
                compute(currOpen+1, currClosed)
                stack.pop()
            if currClosed<currOpen:
                stack.append(")")
                compute(currOpen, currClosed+1)    
                stack.pop()
        
        compute(0,0)
        return result
