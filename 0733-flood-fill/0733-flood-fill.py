class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        rows=len(image)
        cols=len(image[0])
        original_color=image[sr][sc]
        if original_color==color:
            return image
        def dfs(row,col):
            if row<0 or row>=rows or col <0 or col>=cols:
                return
            if image[row][col]!=original_color:
                return
            image[row][col]=color

            dfs(row-1,col) #up
            dfs(row+1,col) #down
            dfs(row,col-1) #left
            dfs(row,col+1) #right

        dfs(sr,sc)

        return image



    