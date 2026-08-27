class Solution(object):
    def numEnclaves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows=len(grid)
        cols=len(grid[0])
        def dfs(row,col):
            if (
                row<0 or row>=rows or
                col<0 or col>=cols or
                grid[row][col]==0
            ):
                return
            grid[row][col]=0

            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col-1)
            dfs(row,col+1)

        for row in range(rows): #Remove the land connected to left and right boundaries
            dfs(row,0)
            dfs(row,cols-1)

        for col in range(cols): #Remove the land connected to top and bottom
            dfs(0,col)
            dfs(rows-1,col)
        
        #count remaining land
        count=0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    count+=1
        return count

        