# add root -> left boundary-> Leaf Nodes-> Right Boundary


class Solution:
    def boundaryTraversal(self, root):
        
        if not root:
            return []
            
        def isLeaf(node):
            return not node.left and not node.right
            
        ans=[]
        
        # Case 1 root
        if not isLeaf(root):
            ans.append(root.data)
        
        # Case 2 left Boundary
        cur=root.left
        while cur:
            if not isLeaf(cur):
                ans.append(cur.data)
            if cur.left:
                cur=cur.left
            else:
                cur=cur.right
            
        # case 3 Leaf Nodes
        def addLeaf(node):
            if not node:
                return
            if isLeaf(node):
                ans.append(node.data)
                return
            addLeaf(node.left)
            addLeaf(node.right)
            
        addLeaf(root)
        
        # Case 4 Right Boundary
        cur=root.right
        stack=[]
        while cur:
            if not isLeaf(cur):
                stack.append(cur.data)
            if cur.right:
                cur=cur.right
            else:
                cur=cur.left

        while stack:
            ans.append(stack.pop())
        
        return ans
        
        
