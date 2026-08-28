class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows=len(grid)
        cols=len(grid[0])

        cnt=0

        def dfs(r,c):
            
            #Out of Bounds
            if r<0 or r>=rows or c<0 or c>=cols:
                return

            #Water already visited
            if grid[r][c]=="0":
                return

            #Mark current land as 0
            grid[r][c]="0"

            #Explore all 4 directions
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        #check every cell
        for r in range(rows):
            for c in range(cols):

                #Found a new island
                if grid[r][c]=="1":
                    cnt+=1
                    dfs(r,c)
        return cnt         