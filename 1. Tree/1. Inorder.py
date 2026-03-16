# https://neetcode.io/problems/binary-tree-inorder-traversal?list=neetcode250

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if root==None:
                return 
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)

        ans=[]
        dfs(root)
        return ans
#-----------------------------------------------------------------
# Non Recursive


class Solution:
    def inOrder(self, root):
        st=[]
        cur=root
        ans=[]
        
        while cur or st:
            while cur:
                st.append(cur)
                cur=cur.left
                
            cur=st.pop()
            ans.append(cur.data)
            cur=cur.right
            
        return ans
