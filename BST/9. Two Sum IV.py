
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hs=set()

        queue=deque([root])
        while queue:

            node=queue.popleft()
            if (k-node.val) in hs:
                return True
            
            hs.add(node.val)

            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
            
        return False        
            
