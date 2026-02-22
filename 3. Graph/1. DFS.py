#https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1


# Recursive
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


# Non Recursive

class Solution:
    def dfs(self, adj):
        
        n = len(adj)
        visited = [False] * n
        ans = []  
        stack = [0]          # start from node 0
        
        while stack:
            v = stack.pop()
            
            if not visited[v]:
                visited[v] = True
                ans.append(v)
                
                # push neighbors in reverse order
                for u in reversed(adj[v]):
                    if not visited[u]:
                        stack.append(u)
        
        return ans
