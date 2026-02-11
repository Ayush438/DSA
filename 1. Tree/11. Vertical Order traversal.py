
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        temp=defaultdict(list)
        queue=deque([(root,0,0)])
        minI=maxI=0
        # dict[[height,row,col]]=[nodes]

        while queue:
                node,row,col=queue.popleft()
                temp[col].append((row,node.val))
                
                minI=min(col,minI)
                maxI=max(col,maxI)
                
                if node.left:
                    queue.append((node.left,row+1, col-1))
                if node.right:
                    queue.append((node.right,row+1, col+1))

        ans=[]
        for c in range(minI,maxI+1):
            temp[c].sort()
            ans.append([val for row,val in temp[c]])

        return ans
