class Solution:
    def timeToBurnTree(self, root, start):

        parent={}
        startNode=None
        def dfs(node, par):
            nonlocal startNode
            if not node:
                return
            parent[node]=par
            if node.data==start:
                startNode=node
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)
        
        visited={startNode}
        queue=deque([startNode])
        ans=0

        while queue:
            n=len(queue)
            burned=False
            for _ in range(n):
                node=queue.popleft()
                for nei in (node.left, node.right, parent[node]):
                    if nei and nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
                        burned=True


            if burned:
                ans+=1
                

        return ans

