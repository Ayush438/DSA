# https://neetcode.io/problems/binary-tree-vertical-order-traversal?list=neetcode250

# Use BFS
# Use hashset to track col no
# root as col 0 and left child col= root-1, right child=root=1  

def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []

        col_no=defaultdict(list)
        queue=deque([(root,0)])

        while queue:
            node, col=queue.popleft()

            if node.left:
                queue.append((node.left,col-1))
            if node.right:
                queue.append((node.right,col+1))
            col_no[col].append(node.val)
        
        temp=sorted(col_no.keys())
        return [col_no[col] for col in temp]
