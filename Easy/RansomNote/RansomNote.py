#https://leetcode.com/problems/ransom-note/

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         if len(magazine) < len(ransomNote):
#             return False

#         letters = [0]*26

#         for i in range(0, len(magazine)):
#             letters[ord(magazine[i]) - ord('a')] = letters[ord(magazine[i]) - ord('a')]+1

#         for i in range(0,len(ransomNote)):
#             if letters[ord(ransomNote[i]) - ord('a')] == 0:
#                 return False
#             else:
#                 letters[ord(ransomNote[i]) - ord('a')] = letters[ord(ransomNote[i]) - ord('a')]-1

#         return True

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return Counter(ransomNote) <= Counter(magazine)

# Counter(ransomNote) creates a dictionary where the keys are the characters in ransomNote, and the values are the counts of each character.

# Similarly, Counter(magazine) creates a dictionary with the counts of each character in magazine.

# The comparison Counter(ransomNote) <= Counter(magazine) checks if all the counts of characters in ransomNote are less than or equal to the counts of the corresponding characters in magazine. If this condition is true, it means that there are enough characters in magazine to construct ransomNote.

# The method returns True if the condition is met (meaning ransomNote can be constructed from magazine), and False otherwise.