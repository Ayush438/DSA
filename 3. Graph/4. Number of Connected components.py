Step 1: Build adjacency list
Step 2: Traverse graph using BFS or DFS
Step 3: Count components



from Collections import defaul, deque
class Solution:
    def findNumberOfComponent(self, V, edges):
        
        graph=default(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visisted=set()
        ans=0

        for node in range(V):
            if node not in visited:
                ans+=1
                queue=deque([node])
                visisted.add(node)

                while queue:
                    cur=queue.popleft()
                    for ed in grapg[cur]:
                        if ed not in visited:
                            visited.add(ed)
                            queue.append(ed)
        return ans

       
