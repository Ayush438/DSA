#  https://leetcode.com/problems/target-sum/description/

#    dp[sum]=no of ways possible

#  arr=[1 1 1 1 1]
#
#  dp[0]=1   +1= 1              --->  dp[+1]=1        dp[+1]  +1=2       --->dp[0]=2
#            -1=-1              --->  dp[-1]=1                -1=0       --->dp[-2]=1
#                                                                        --->dp[2]=1
#                                                     dp[-1]  +1=0
#                                                             -1=-2
#

 def findTargetSumWays(self, nums, target):
        tempDict={}
        tempDict[0]=1

        for i in nums:
            tempDict2={}

            for j in tempDict.keys():
                tempDict2[j+i]=tempDict2.get(j+i,0) + tempDict[j]
                tempDict2[j-i]=tempDict2.get(j-i,0)+ tempDict[j]
            tempDict=tempDict2
        return tempDict.get(target,0)
