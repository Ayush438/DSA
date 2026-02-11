


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=[]
        queue=deque([(root,str(root.val))])

        while queue:
             node, path=queue.popleft()

             if not node.left and not node.right:
                ans.append(path)

             if node.left:
                queue.append((node.left,path+"->"+str(node.left.val)))

             if node.right:
                queue.append((node.right,path+"->"+str(node.right.val)))

        return ans
