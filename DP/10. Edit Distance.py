#  https://leetcode.com/problems/edit-distance/description/

#      | ""| a  |  b | c  |  d |  e  |  f  |
#    ""| 0 | 1  |  2 | 3  |  4 |  5  |  6  |      -->no of operations to convert string A to B (eg. 6 delete opr to make "abcded" to ""
#    a | 1 | 0  |  1 | 2  |  3 |  4  |  5  |        # example convert ab-> az   1. 1+(ab->a)  =1+(ramove b)
#    z | 2 | 1  |  1 | 2  |  3 |  4  |  5  |                                    2. 1+(az->a)  =1+(remove z)                ==> take min of all three
#    c | 3 | 2  |  2 | 1  |  2 |  3  |  4  |                                    3. 1+(a->a)   =1+(replace b with z)
#    d | 4 | 3  |  3 | 2  |  1 |  2  |  3  |         # if both char are same then dp[i][j]=dp[i-1][j-1]  --> no operation 
#    e | 5 | 4  |  4 | 3  |  2 |  1  |  2  |         # ans=dp[n][n]=2


    def minDistance(self, word1, word2):
        n,m=len(word1), len(word2)
        dp=[[0]*(m+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0]=i
        for j in range(m+1):
            dp[0][j]=j

        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=1+min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        return dp[n][m]
