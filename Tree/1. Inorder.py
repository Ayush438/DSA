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
