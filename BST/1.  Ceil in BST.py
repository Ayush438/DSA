 
class Solution:
    def findCeil(self,root, x):
        ans=-1
        
        
        while root:
            if root.data==x:
                return x
                
            if root.data>x:
                ans=root.data
                root=root.left
            else:
                root=root.right

        return ans
