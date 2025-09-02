#  https://leetcode.com/problems/longest-increasing-subsequence/description/

                                                                                       #Defult value dp is 1
#    3  4  -1  0  6  2  3                                                              #start i at index 1 and j at 0
# dp [1  2  1  1  1  1  1]                                                             #if a[j]<a[i] then dp[i]=d[j]+1,  till i==j
#  i=1   j=0                                                                           # then reset j=0 and i++

#  dp [1  2  1  1  1  1  1]    dp [1  2  1  1  1  1  1]  
#  i=2   j=0                      i=2   j=1

#  dp [1  2  1  1  1  1  1]    dp [1  2  1  1  1  1  1]     dp [1  2  1  2  1  1  1]  
#  i=3   j=0                      i=3   j=1                    i=3   j=2

#  dp [1  2  1  2  2  1  1]    dp [1  2  1  2  3  1  1]    dp [1  2  1  2  3  1  1]   dp [1  2  1  2  3  1  1] 
#  i=4   j=0                      i=4   j=1                    i=4   j=2                     i=4   j=3



 def lengthOfLIS(self, nums):
        n=len(nums)
        dp=[1]*n
        ans=1

        for i in range(1,n):
            for j in range(0,i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[j]+1, dp[i])
                    ans=max(dp[i],ans)
        return ans
