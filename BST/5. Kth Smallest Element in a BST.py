class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st=[]
        cur=root

        while st or cur:
            
            while cur:
                st.append(cur)
                cur=cur.left

            cur=st.pop()
            k-=1
            if k==0:
                return cur.val

            cur=cur.right
