class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorder_index={val:idx for idx, val in enumerate(inorder)}
        self.pre_idx=0

        def build(left, right):
            if left>right:
                return None

            node_val=preorder[self.pre_idx]
            self.pre_idx+=1

            node=TreeNode(node_val)
            mid=inorder_index[node_val]

            node.left=build(left,mid-1)
            node.right=build(mid+1,right)

            return node
            
        return build(0,len(inorder)-1)
