class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        inorder_index={val:idx for idx,val in enumerate(inorder)}
        self.post_idx=len(postorder)-1

        def build(left, right):
            if left>right:
                return None

            node_val=postorder[self.post_idx]
            self.post_idx-=1
            node=TreeNode(node_val)

            mid=inorder_index[node_val]
            node.right=build(mid+1, right)
            node.left=build(left, mid-1)
            
            return node
        
        return build(0, len(postorder)-1)
