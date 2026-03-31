1. Build an adjacency list from the given edge list to represent the undirected graph.
2. Maintain a visited set to track already explored nodes.
3. Run BFS/DFS from each unvisited node, keeping track of the parent node.
4. If a visited neighbor is found that is not the parent, a cycle exists.




from collections import defaultdict, deque

class Solution:
	def isCycle(self, V, edges):
		#Code here
		graph=defaultdict(list)
		
		for u,v in edges:
		    graph[u].append(v)
		    graph[v].append(u)
		   
		visited=set()
		    
        for u in range(V):
            if u in visited:
                continue
		    
		    queue=deque([(u,-1)])
		    while queue:
		        node, parent=queue.popleft()
		    
		        if node in visited:
		            continue
		      
		        visited.add(node)
		        
		        for i in graph[node]:
		            if i not in visited:
		                queue.append((i,node))
		            elif i!=parent: 
                        return True
		            
		return False
		        
