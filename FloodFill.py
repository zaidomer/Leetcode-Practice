#https://leetcode.com/problems/flood-fill

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        oldColor = image[sr][sc]

        if oldColor==color:
            return image

        image[sr][sc] = color
        # print(str(sr) + ", " + str(sc))
        # print(image)
        
        if (sr-1 >= 0) and image[sr-1][sc]==oldColor: #left
            image = self.floodFill(image, sr-1, sc, color)
        if (sr+1 < len(image)) and image[sr+1][sc]==oldColor: #right
            image = self.floodFill(image, sr+1, sc, color)
        if (sc-1 >= 0) and image[sr][sc-1]==oldColor: #up
            image = self.floodFill(image, sr, sc-1, color)
        if (sc+1 < len(image[0])) and image[sr][sc+1]==oldColor: #down
            image = self.floodFill(image, sr, sc+1, color)

        return image