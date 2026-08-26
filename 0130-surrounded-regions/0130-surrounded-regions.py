class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return 
        m=len(board)
        n=len(board[0])

        def dfs(r,c):
            if r<0 or r>=m or c<0 or c>=n:
                return
            if board[r][c]!='O':
                return
            
            board[r][c]="S"
            
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        
        #first row
        for c in range(n):
            if board[0][c]=="O":
                dfs(0,c)
        
        #Last row
        for c in range(n):
            if board[m-1][c]=='O':
                dfs(m-1,c)
        
        #First column
        for r in range(m):
            if board[r][0]=="O":
                dfs(r,0)
        
        #Last column
        for r in range(m):
            if board[r][n-1]=='O':
                dfs(r,n-1)
        
        for r in range(m):
            for c in range(n):
                if board[r][c]=='O':
                    board[r][c]='X'
                
                elif board[r][c]=='S':
                    board[r][c]='O'








        