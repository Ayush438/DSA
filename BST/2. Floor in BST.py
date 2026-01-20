
class Solution:
    def floor(self, root, x):
        ans=-1
        
        while root:
            if root.data==x:
                return x
            
            if root.data>x:
                root=root.left
            else:
                ans=root.data
                root=root.right
        return ans
