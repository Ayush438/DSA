#BST rule is global, not local
#Each node must lie within a valid range:

#(min < node.val < max)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bst(root, low, high):
            if not root:
                return True
            
            if not (low < root.val < high):
                return False

            return bst(root.left, low, root.val) and bst(root.right, root.val, high)
        
        return bst(root, -float('inf'), float('inf'))
