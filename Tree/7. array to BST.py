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
