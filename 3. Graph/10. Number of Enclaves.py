class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ans=0
        n,m=len(grid), len(grid[0])


        def dfs(i,j):
            if i<0 or j<0 or i>=n or j>=m or grid[i][j]!=1:
                return
            
            grid[i][j]=2

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

        print(grid)
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    ans+=1
                
        return ans
