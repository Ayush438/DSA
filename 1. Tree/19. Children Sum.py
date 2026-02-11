Input: root = [10,4,6,1,3,2,4]
Output: true

4 = 1 + 3
6 = 2 + 4
10 = 4 + 6
All internal nodes satisfy the condition.


class Solution:
    def checkChildrenSum(self, root: TreeNode) -> bool:

        def dfs(root):
            if not root:
                return 0
            if  not root.left and not root.right:
                return root.val
            left=dfs(root.left)
            if left==-1:
                return -1
            right=dfs(root.right)
            if right==-1:
                return -1
            if root.val!=(left+right):
                return -1
            return root.val
        
        return dfs(root)!=-1
