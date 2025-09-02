#  https://leetcode.com/problems/min-cost-climbing-stairs/submissions/1757364236/

#  dp[i]= min(  cost at (i-1)+cost to reach(i-1),   cost at (i-1)+cost to reach(i-1))

 def minCostClimbingStairs(self, cost):
        n=len(cost)
        dp=[0]*(n+1)

        for i in range(2,n+1):
            dp[i]=min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[n]
