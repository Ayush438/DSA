
BFS start node	target
Infinite traversal	visited set
Extra nodes	continue when dist == k


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []

        queue=deque([(target,0)])
        visited={target}
        parent={}
        ans=[]

        #Create parent dict
        def dfs(node,par):
            if not node:
                return 
            parent[node]=par
            dfs(node.left,node)
            dfs(node.right,node)
        
        dfs(root,None)

        # Traverse
        while queue:
            node, dis=queue.popleft()
            if dis==k:
                ans.append(node.val)

            for neb in (node.left, node.right, parent[node]):
                if neb and neb not in visited:
                    visited.add(neb)
                    queue.append((neb,dis+1))
            
        return ans
