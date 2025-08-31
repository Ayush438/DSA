# https://leetcode.com/problems/coin-change/

#Greedy approach will fail : [1 5 6 9]  target =11

#DP approach:  |amount|  0   1  2  3  4  5  6  7  8  9  10  11  |
#  min coin    |      |  0   1  2  3  4  1  1  2  3  1   2   3

# amountto make=  5
#coin choice  =    case1 choose coin1              | case2 choose coin 5
#                      1+ DP[4]  =1+4=5            |  1+DP[0]=1    
# min (1,5)=1

def coinChange(self, coins, amount):
        if amount==0: return 0

        dp=[0]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            dp[i]=sys.maxsize
            for j in coins:
                if (i-j)>=0 and dp[i-j]!=sys.maxsize:
                    dp[i]=min(dp[i],1+dp[i-j])

        if dp[amount]==sys.maxsize: return -1
        return dp[amount]
            
