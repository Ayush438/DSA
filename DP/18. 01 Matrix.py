#  https://leetcode.com/problems/01-matrix/description/


#Input
#        inf  inf  inf   inf   inf   inf    inf           
#-------------------------------------------------
# inf |     |  0  |     |     |     |     |     |   
# inf |     |     |     |     |     |     |  0  |   
# inf |     |     |     |  0  |     |     |     |   
# inf |     |     |     |     |     |     |     |   

Travel top to bottom
#        inf  inf  inf   inf   inf   inf    inf           
#-------------------------------------------------                  #dp1[n][m]=  min(dp1[n-1][m],  dp1[n][m-1] ) +1
# inf |  inf|  0  |  1  |  2  |  3  |  4  |  5  |   
# inf |  inf|  1  |  2  |  3  |  4  |  5  |  0  |   
# inf |  inf|  2  |  3  |  0  |  1  |  2  |  1  |   
# inf |  inf|  3  |  4  |  1  |  2  |  3  |  2  |   

Travel bottom to top
#        inf  inf  inf   inf   inf   inf    inf           
#-------------------------------------------------                  #dp2[n][m]= min(  min(dp2[n+1][m],  dp2[n][m+1]) +1, dp1[n][m] )
# inf |   1 |  0  |  1  |  2  |  3  |  2  |  1  |   inf
# inf |   2 |  1  |  2  |  1  |  2  |  1  |  0  |   inf
# inf |   3 |  2  |  1  |  0  |  1  |  2  |  1  |   inf
# inf |   4 |  3  |  4  |  1  |  2  |  3  |  2  |   inf
# inf |  inf| inf | inf | inf | inf | inf | inf |   inf


class Solution(object):
    def updateMatrix(self, mat):
        row, col=len(mat), len(mat[0])
        dp=[[sys.maxsize]*(col) for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if mat[i][j]==0:
                    dp[i][j]=0

        for i in range(row):
            for j in range(col):
                if dp[i][j]!=0:
                    if i>0:
                        dp[i][j]=min(dp[i][j], dp[i-1][j]+1)
                    if j>0:
                        dp[i][j]=min(dp[i][j], dp[i][j-1]+1)

        for i in range(row-1,-1,-1):
            for j in range(col-1,-1, -1):
                if mat[i][j]!=0:
                    if i<row-1:
                        dp[i][j]= min(dp[i][j], dp[i+1][j]+1)
                    if j<col-1:
                        dp[i][j]= min(dp[i][j], dp[i][j+1]+1)

        return dp


        
