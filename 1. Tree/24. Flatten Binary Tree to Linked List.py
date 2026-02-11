class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:

       if not root:
            return None
       queue=deque([root])
       ln=rn=None
       temp=None

       while queue:
            node=queue.popleft()
            ln=node.left
            rn=node.right
            if temp:
                temp.right=node
                
            temp=node
            temp.left=None

            if rn:
                queue.insert(0,rn)
            if ln:
                queue.insert(0,ln)
            
        #root=root.right
