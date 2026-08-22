from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """        
        rows=len(grid)
        cols=len(grid[0])

        queue=deque()
        fresh=0
        mins=0


        #Find the rotten oranges and count fresh oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1

        #Directions for 4 directional movement
        directions=[
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]


        #Multi Source BFS
        while queue and fresh >0:
            size=len(queue)
            #process all oranges of the current mins
            for _ in range(size):
                row,col=queue.popleft()

                #Check all 4 neighbours
                for dr,dc in directions:
                    new_row=row+dr
                    new_col= col+dc
                    #Check boundries
                    if(new_row>=0 and new_row<rows and  new_col>=0 and new_col<cols and grid[new_row][new_col]==1):
                        
                        

                    #Make fresh oranges rotten
                        grid[new_row][new_col]=2

                        #one less fresh orange
                        fresh-=1

                        #Add newly rotten oranges
                        queue.append((new_row,new_col))
            #One Bfs level completed
            mins+=1
        #If fresh oranges remain, impossible
        if fresh>0:
            return -1

        return mins

    
        
            

                
