# https://neetcode.io/problems/balanced-binary-tree?list=neetcode250


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if root==None:
                return 0
            left=check(root.left)
            if left==-1:
                return -1
            right=check(root.right)
            if right==-1:
                return -1

            if abs(left-right)>1:
                return -1
            return 1+max(left,right)
        return check(root)!=-1

