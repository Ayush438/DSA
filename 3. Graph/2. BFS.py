class Solution:
    def bfs(self, adj):
        # code here
        
        ans=[]
        queue=deque([0])
        visited=[False]*(len(adj))
        visited[0]=True
        
        
        while queue:
            v=queue.popleft()
            visited[v]=True
            ans.append(v)
            
            for u in adj[v]:
                if visited[u]==False:
                    visited[u]=True
                    queue.append(u)
                
        return ans
