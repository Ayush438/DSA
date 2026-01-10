class Solution:
    def topView(self, root):
        
        if not root:
            return []
            
        hdMap={}
        queue=deque([(root,0)])
        minI=maxI=0
        
        while queue:

                node,dis=queue.popleft()
                if dis not in hdMap:
                    hdMap[dis]=node.data
                
                minI=min(minI,dis)
                maxI=max(maxI,dis)
                
                if node.left:
                    queue.append((node.left,dis-1))
                if node.right:
                    queue.append((node.right,dis+1))
        
        
        return [hdMap[c] for c in range(minI, maxI+1)]
        
