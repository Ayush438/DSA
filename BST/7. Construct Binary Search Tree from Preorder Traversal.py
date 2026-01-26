
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        self.idx=0

        def dfs(preorder, low, high):
            if self.idx==len(preorder) or not (low < preorder[self.idx] < high):
                return
            
            node=TreeNode(preorder[self.idx])

            self.idx+=1
            node.left=dfs(preorder, low, node.val)
            node.right=dfs(preorder, node.val, high)
            return node

        return dfs(preorder, -float('inf'), float('inf'))
