class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        temp=root

        while temp:
            if temp.val>val:
                if temp.left==None:
                    temp.left=TreeNode(val)
                    break
                else:
                    temp=temp.left
            else:
                if temp.right==None:
                    temp.right=TreeNode(val)
                    break
                else:
                    temp=temp.right
        return root
