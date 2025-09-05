# https://leetcode.com/problems/maximal-square/description/

#    if i==0 or j==0 then dp[i][j]=index[i][j]
#    if index[i][j]==1, then check for min( index[i-1][j], index[i-1][j-1], index[i][j-1] ) + 1
#    

Input:

#  1  |  0  |  1  |  0  |  0  |                        |  1  |  0  |  1  |  0  |  0  |
#  1  |  0  |  1  |  1  |  1  |                        |  1  |  0  |  1  |  1  |  1  |
#  1  |  1  |  1  |  1  |  1  |      ==>               |  1  |  1  |  1  |  2  |  2  |
#  1  |  0  |  1  |  1  |  1  |                        |  1  |  0  |  1  |  2  |  3  |
#

class Solution(object):
    def maximalSquare(self, matrix):

        row, col= len(matrix), len(matrix[0])
        dp=[[0]*col for _ in range(row)]
        ans=0

        for i in range(row):
            for j in range(col):
                if i==0 or j==0:
                    dp[i][j]=int(matrix[i][j])
                elif matrix[i][j]=="1":
                    dp[i][j]= min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) +1
                ans=max(ans, dp[i][j])

        return ans*ans
        
