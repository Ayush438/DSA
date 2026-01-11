class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue=deque([(root,0)])
        temp={}
        
        while queue:
            node,order=queue.popleft()

            if order not in temp:
                temp[order]=node.val

            if node.right:
                queue.append((node.right,order+1))
            if node.left:
                queue.append((node.left,order+1))
        
        return [temp[i] for i in range(len(temp))]
