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
#-----------------------------------------------------------------
# Non Recursive


class Solution:
    def inOrder(self, root):
        st=[]
        cur=root
        ans=[]
        
        while cur or st:
            while cur:
                st.append(cur)
                cur=cur.left
                
            cur=st.pop()
            ans.append(cur.data)
            cur=cur.right
            
        return ans

#-----------------------------------------------------------------
# Pre order

class Solution:
    def preOrder(self, root):
        if not root:
            return []

        stack = [root]
        ans = []

        while stack:
            node = stack.pop()
            ans.append(node.data)

            if node.right:
                stack.append(node.right)

            if node.left:
                stack.append(node.left)

        return ans


#---------------------------------------------------------
#Post order (Two Stack)

class Solution:
    def postOrder(self, root):
        if not root:
            return []

        stack1 = [root]
        stack2 = []
        ans = []

        while stack1:
            node = stack1.pop()
            stack2.append(node)

            if node.left:
                stack1.append(node.left)

            if node.right:
                stack1.append(node.right)

        while stack2:
            ans.append(stack2.pop().data)

        return ans
