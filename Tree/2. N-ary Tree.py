# https://neetcode.io/problems/n-ary-tree-postorder-traversal?list=neetcode250



class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(root):
            if root==None:
                return
            for child in root.children:
                dfs(child)
            ans.append(root.val)
            
        ans=[]
        dfs(root)
        return ans
