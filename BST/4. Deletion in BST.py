
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val > key:
            root.left=self.deleteNode(root.left, key)
        elif root.val < key:
            root.right=self.deleteNode(root.right, key)
        else:

        # case 2 & 3 (0 child or 1 child)
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
        
        # case 1 (2 childs)
            temp=root.right
            while temp.left:
                temp=temp.left

            root.val=temp.val
            root.right=self.deleteNode(root.right, temp.val)      
            
        return root


      4
     / \
    3   8
       / \
      6   10
     /
    4   ← duplicate!
