# https://neetcode.io/problems/binary-tree-vertical-order-traversal?list=neetcode250

# Use BFS
# Use hashset to track col no
# root as col 0 and left child col= root-1, right child=root=1  

def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []

        col_table=defaultdict(list)
        queue=deque([(root,0)])

        while queue:
            node, col=queue.pop()
            col_table[col].append(node.val)

            if node.right:
                queue.append((node.right,col+1))
            if node.left:
                queue.append((node.left,col-1))

        temp=sorted(col_table.keys())

        return [col_table[col] for col in temp]
