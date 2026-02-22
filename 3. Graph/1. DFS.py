#https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1

class Solution:
    def dfs(self, adj):
        def traverse(v, adj, visited, ans):
            
            visited[v]=True
            ans.append(v)
            
            for u in adj[v]:
                if visited[u]==False:
                    traverse(u,adj,visited,ans)
               
        n=len(adj)
        visited=[False]*(n)
        ans=[]
        traverse(0,adj,visited,ans)
        return ans
            
