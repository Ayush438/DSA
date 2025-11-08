# https://neetcode.io/problems/single-number-iii?list=neetcode250

1. Xor or all element
2. Find right most set bit in xor  (xor and -xor)
3. For each element if that bit is set a^=arr[i] else b^=arr[i]


 def singleNumber(self, nums: List[int]) -> List[int]:
        x=0
        ans=[0,0]
        for num in nums:
            x^=num
        
        x=x & -x

        for num in nums:
            if num & x:
                ans[0]=ans[0] ^num
            else:
                ans[1]=ans[1] ^num
        return ans
