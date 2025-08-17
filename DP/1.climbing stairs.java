//  https://leetcode.com/problems/climbing-stairs/

//if n==1 ans=1, {1}
//if n==2 ans=2, {(1,1), (2)}
//if n==3 ans=3, {(1,1,1), (2,1),(1,2)}
//if n==4 ans=4, {(1,1,1,1), (1,2,1),(2,1,1), (1,1,2), (2,2)}

//  for ex. to reach 4 =  (no of ways to reach 3th) or (no of ways to reach 2th)
//                     =   3 +2  =5


public int climbStairs(int n)
  {      
        if(n<3) return n;
        int x=1, y=2, ans=0;

        for(int i=3;i<=n;i++)
        {
            ans=x+y;
            x=y;
            y=ans;
        }
        return ans;
    }

//----------------------------------------------------
//   DP solution
public int climbStairs(int n) {

    if (n == 1) return 1;

    int[] dp = new int[n + 1];
    dp[1] = 1;
    dp[2] = 2;

    for (int i = 3; i <= n; i++) {
      dp[i] = dp[i - 1] + dp[i - 2];
    }

    return dp[n];
  }
