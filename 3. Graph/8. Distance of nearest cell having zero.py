# Bfs appraoch, Steps:
#1. Push all 0s into queue
#2. Mark all 1s as ∞ (unvisited)
#3. Run BFS:
#4. For each cell, visit neighbors
#5. Update distance = current + 1

class Solution:
    def updateMatrix(self, mat):
        m, n = len(mat), len(mat[0])
        queue = deque()

        # Step 1: Initialize
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = float('inf')

        # Directions
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        # Step 2: BFS
        while queue:
            x, y = queue.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    if mat[nx][ny] > mat[x][y] + 1:   #Can I reach (nx, ny) with a shorter distance through (x, y)?”
                        mat[nx][ny] = mat[x][y] + 1
                        queue.append((nx, ny))

        return mat

#------------------------------------------------------------------------------------------

#Dp approach
#1. Initialize dp: 0 for cells with 0, else ∞
#2. First pass (top-left → bottom-right): update using top & left neighbors
#3. Second pass (bottom-right → top-left): update using bottom & right neighbors
#4. Return dp as final shortest distances


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n,m=len(mat), len(mat[0])
        dp=[[float('inf')]*(m) for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    dp[i][j]=0
                else:
                    if i>0:
                        dp[i][j]=min(dp[i][j],dp[i-1][j]+1)
                    if j>0:
                        dp[i][j]=min(dp[i][j],dp[i][j-1]+1)

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if mat[i][j]==0:
                    dp[i][j]=0
                else:
                    if i<n-1:
                        dp[i][j]=min(dp[i][j],dp[i+1][j]+1)
                    if j<m-1:
                        dp[i][j]=min(dp[i][j],dp[i][j+1]+1)
        return dp
