class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=1
        queue=deque([(root,0)])

        while queue:
            n=len(queue)
            _,first=queue[0]
            _,last=queue[-1]
            ans=max(ans,last-first+1)

            for _ in range(n):
                node, pos=queue.popleft()

                if node.left:
                    queue.append((node.left,2*pos))
                if node.right:
                    queue.append((node.right, 2*pos+1))
                
        return ans
