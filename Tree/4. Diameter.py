# https://neetcode.io/problems/binary-tree-diameter?list=neetcode250

def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def height(root):
            if root==None:
                return 0

            nonlocal ans
            Hleft=height(root.left)
            Hright=height(root.right)
            ans=max(ans, Hleft+ Hright)

            return 1+max(Hleft, Hright)

        height(root)
        return ans
