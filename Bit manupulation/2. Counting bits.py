# https://neetcode.io/problems/counting-bits?list=neetcode250

# Brian Kernighan’s bit-count  o(nlong n)
def countBits(self, n: int) -> List[int]:
        ans=[0]*(n+1)
        for num in range(1,n+1):
            temp=num
            count=0
            while temp>0:
                temp= temp & (temp-1)
                count+=1
            ans[num]=count
        return ans


#---------------------------------------------
#DP solution o(n)  
#Every integer x can be represented as:
 #           x = (x >> 1) * 2 + (x & 1)
#DP Recurrence
#countBits[i] = countBits[i >> 1] + (i & 1)

    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
