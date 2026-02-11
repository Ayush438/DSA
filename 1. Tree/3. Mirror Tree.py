# https://neetcode.io/problems/invert-a-binary-tree?list=neetcode250


    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root==None:
            return 
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.right, root.left=root.left, root.right

        return root
