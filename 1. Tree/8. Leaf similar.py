# https://leetcode.com/problems/leaf-similar-trees/submissions/1822730121/

def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        left,right=[],[]

        def support(root, temp):
            if root==None:
                return
            if root.left==None and root.right==None:
                temp.append(root.val)
                return
            support(root.left, temp)
            support(root.right, temp)
        
        support(root1,left)
        support(root2,right)

        return left==right
