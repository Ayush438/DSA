# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/1822675659/

def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def bst(i,j):
            if i>j:
                return None
            mid=(i+j)//2
            node=TreeNode(nums[mid])
            node.left=bst(i,mid-1)
            node.right=bst(mid+1,j)
            return node
        
        if not nums:
            return None
        return bst(0,len(nums)-1)



--------------------------------------------------------------------
# https://neetcode.io/problems/merge-two-binary-trees?list=neetcode250

def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(root1 ,root2):
            if root1==None and root2==None:
                return None
            
            if root1==None:
                return root2
            if root2==None:
                return root1
            
            node=TreeNode(root1.val+root2.val)
            node.left=merge(root1.left,root2.left)
            node.right=merge(root1.right,root2.right)
            return node

        return merge(root1, root2)
