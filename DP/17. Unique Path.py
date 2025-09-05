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
