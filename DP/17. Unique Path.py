#  https://leetcode.com/problems/unique-paths/description/

#  0  |  1  |  2  |  3  |  4  |  5  |
#-------------------------------------
#  1  |  1  |  1  |  1  |  1  |  1  |
#  2  |  1  |  2  |  3  |  4  |  5  |        # so dp[n][m]=  dp[n-1][m]  +  dp[n][m-1]
#  3  |  1  |  3  |  6
#  4  |  1  |
#  5  |  1  |

   def uniquePaths(self, m, n):
        dp=[[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            for j in range(n+1):
                if  i==1 or j==1:
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j]+ dp[i][j-1]
        return dp[m][n]


---------------------------------------------------------------------------------------------------------------

#https://leetcode.com/problems/unique-paths-ii/description/?envType=problem-list-v2&envId=dynamic-programming


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        n,m=len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0

        dp=[[0]*(m) for _ in range(n)]
        dp[0][0]=1

        for i in range(1,n):
            dp[i][0]=0 if obstacleGrid[i][0]==1 else dp[i-1][0]

        for i in range(1,m):
            dp[0][i]=0 if obstacleGrid[0][i]==1 else dp[0][i-1]

        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]

        return dp[n-1][m-1]
        
