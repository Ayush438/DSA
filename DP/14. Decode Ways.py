#  https://leetcode.com/problems/decode-ways/description/

#                                                122016                                  #digit can be of size 1 or 2 because of A-Z==1-26
#                                          1    /      \      12                         #So divide in such a way, either size 1 or size 2
#                                           22016        2016
#                                    2  /     22 \     2  /      \  20
#                                    2016      016    016        16
#                                 2/   \  20     |
#                                016     16        invalid, because digit will not start from 0     
#                             invalid    /\ 
#                                    1 /    \ 16
#                                    6      "" --empty string                           # if able to rach empty string that  means able to decode entire string  
#                                    |                                                  #How many emty strings we are getting, those many decodes are possible
#                                   ""
-----------------------------------------------------------------------------------------------------
#  Memorization tecnique:
#      ways todecode[i]= ways todecode[i-1] (if new single digit is vaild)+ ways todecode[i-2] (if new last two digit is vaild)


#                1    2     2    0    1    6                                             #0th index is when input is empty so no of ways for empty string=1
#        |  1  | 1  | 2  |  3  |    |    |                                               #1st index when value is non zero then =1 else =0  
#index      0    1    2    3    4    5      6  
----------------------------------------------------------------------------------------------------
#                1    2     2    0    1    6  
#        |  1  | 1  | 2  |  3  | 2  |  2  | 4                                            #for index(4) valse is zero so we can not map with any character,  
#index      0    1    2    3    4    5      6                                            # dp[4]=0+2=2
#                                                                                        #same for index(5) , 1 is valide but 01 is not
#                                                                                        #dp[5]=2+0=2

def numDecodings(self, s):
        n=len(s)
        if n==0 or s[0]=='0':
            return 0

        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1 if s[0]!='0' else 0

        for i in range(2,n+1):
            x=dp[i-1] if s[i-1]!='0' else 0
            y=dp[i-2] if 10 <= int(s[i-2:i]) <= 26 else 0
            dp[i]=x+y
        return dp[n]
        
