#Traverse boundary cells
#For every 'O' on boundary → run DFS/BFS → mark as 'S' (safe)
#Traverse whole board:
#  'O' → convert to 'X' (captured)
#  'S' → convert back to 'O'

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        n,m=len(board), len(board[0])

        def dfs(i, j):
            if i<0 or i>=n or j<0 or j>=m or board[i][j]!='O':
                return
            board[i][j]='S'

            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        for i in range(n):
            dfs(i,0)
            dfs(i,m-1)

        for j in range(m):
            dfs(0,j)
            dfs(n-1,j)

        for i in range(n):
            for j in range(m):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='S':
                    board[i][j]='O'
