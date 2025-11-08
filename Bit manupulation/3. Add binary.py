# https://neetcode.io/problems/add-binary?list=neetcode250

def addBinary(self, a: str, b: str) -> str:
        carry,sum=0,0
        n,m= len(a), len(b)
        i, j = len(a) - 1, len(b) - 1
        ans=[]

        while i>=0 or j>=0:
            x= int(a[i]) if i>=0 else 0
            y= int(b[j]) if j>=0 else 0
            total=x+y+carry
            ans.append(str(total%2))
            carry=total//2
            i-=1
            j-=1

        return ''.join(ans[::-1])
