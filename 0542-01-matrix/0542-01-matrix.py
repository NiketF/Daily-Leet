from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m=len(mat)
        n=len(mat[0])

        queue=deque()

        #Answer Matrix
        dist=[[-1]* n for _ in range(m)]


        #Put 0 in queue
        for r in range(m):
            for c in range(n):
                if mat[r][c]==0:
                    dist[r][c]=0
                    queue.append((r,c))
        
        #Directions
        direc=[
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]

        #BFS
        while queue:
            r,c=queue.popleft()

            for dr,dc in direc:
                nr=r+dr
                nc=c+dc

                #Check valid and unvisited
                if(
                0<=nr<m and
                0<=nc<n and
                dist[nr][nc]==-1
                ):
                    dist[nr][nc]=dist[r][c]+1
                    queue.append((nr,nc))
        return dist
         
        