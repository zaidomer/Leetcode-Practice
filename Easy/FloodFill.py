#https://leetcode.com/problems/flood-fill

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        self.help(image, visited, sr, sc, color)
        return image

    def help(self, image: List[List[int]], visited: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        og = image[sr][sc]
        image[sr][sc] = color
        visited.add((sr,sc))

        if sr<len(image)-1 and image[sr+1][sc]==og and (sr+1,sc) not in visited:
            self.help(image,visited,sr+1,sc,color)
        if sr>0 and image[sr-1][sc]==og and (sr-1,sc) not in visited:
            self.help(image,visited,sr-1,sc,color)
        if sc<len(image[0])-1 and image[sr][sc+1]==og and (sr,sc+1) not in visited:
            self.help(image,visited,sr,sc+1,color)
        if sc>0 and image[sr][sc-1]==og and (sr, sc-1) not in visited:
            self.help(image,visited,sr,sc-1,color)



    # def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    #     m, n = len(image), len(image[0])
    #     origColor = image[sr][sc]
    #     q = deque([[sr, sc]])
    #     visited = set()
    #     visited.add((sr, sc))
        
    #     while q:
    #         r, c = q.popleft()
    #         image[r][c] = newColor
    #         for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
    #             row, col = r + dr, c + dc
    #             if 0 <= row < m and 0 <= col < n and image[row][col] == origColor and (row, col) not in visited:
    #                 q.append([row, col])
    #                 visited.add((row, col))
    #     return image





    # def floodFill(self, image, sr, sc, color):
    #     """
    #     :type image: List[List[int]]
    #     :type sr: int
    #     :type sc: int
    #     :type color: int
    #     :rtype: List[List[int]]
    #     """
    #     oldColor = image[sr][sc]

    #     if oldColor==color:
    #         return image

    #     image[sr][sc] = color
    #     # print(str(sr) + ", " + str(sc))
    #     # print(image)
        
    #     if (sr-1 >= 0) and image[sr-1][sc]==oldColor: #left
    #         image = self.floodFill(image, sr-1, sc, color)
    #     if (sr+1 < len(image)) and image[sr+1][sc]==oldColor: #right
    #         image = self.floodFill(image, sr+1, sc, color)
    #     if (sc-1 >= 0) and image[sr][sc-1]==oldColor: #up
    #         image = self.floodFill(image, sr, sc-1, color)
    #     if (sc+1 < len(image[0])) and image[sr][sc+1]==oldColor: #down
    #         image = self.floodFill(image, sr, sc+1, color)

    #     return image