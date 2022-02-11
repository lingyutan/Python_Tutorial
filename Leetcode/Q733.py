class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
		# If newColor is the same as oldColor, just return the image as it is
        if oldColor == newColor:
            return image
		# Recursion DFS
        self.DFS(image, sr, sc, newColor, oldColor)

        return image

    def DFS(self, image: List[List[int]], sr : int, sc : int, newColor: int, oldColor: int) -> List[List[int]]:
        while 0 <= sr < len(image) and 0 <= sc < len(image[0]) and image[sr][sc] == oldColor:
            image[sr][sc] = newColor
            for d in [[-1,0], [1,0], [0,-1], [0,1]]:
                self.DFS(image, sr + d[0], sc + d[1], newColor, oldColor)
        return image
        
