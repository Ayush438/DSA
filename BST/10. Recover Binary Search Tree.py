prev → previous node in inorder
first → first wrong node
second → second wrong node
-----------------------------------------
Algo:
1. Perform an inorder traversal
2. Keep track of the previous node
3. Whenever prev.val > current.val, a violation occurs
4. On the first violation, store first = prev
5. On the second violation, store second = current
6. After traversal, swap first.val and second.val

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first=self.second=self.prev =None

        def inorder(root):

            if not root:
                return

            inorder(root.left)
            if self.prev and self.prev.val > root.val:
                if not self.first:
                    self.first=self.prev

                self.second=root
            
            self.prev=root
            inorder(root.right)

        inorder(root)
        self.first.val, self.second.val= self.second.val, self.first.val
            
