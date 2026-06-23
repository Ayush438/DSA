#339. Nested List Weight Sum
'''
def nested_list(nested_list):
    def flattern(_nested_list, level):

        ans=0
        for data in _nested_list:
            if type(data)==int:
                ans+=(data*level)
            else:
                ans+=flattern(data,level+1)
        return ans
    print(flattern(nested_list,1))

nested_list([1,[4,[6]]])'''


#364. Nested List Weight Sum II   https://leetcode.ca/all/364.html

'''def nested_list(nested_list):

    temp=[]
    max_level=0
    ans=0

    def flattern(_nested_list, level):
        
        nonlocal max_level
        max_level=max(max_level, level)

        for node in _nested_list:
            if type(node)==int:
                temp.append((node, level))
            else:
                flattern(node, level+1) 

    flattern(nested_list,0)

    for node, level in temp:
        ans+=(node*(max_level-level+1))
    
    print(ans)

nested_list([1,[4,[6]]])'''
'''-------------------------------------
def nested_list(nested_list):

    max_level = 0

    def find_depth(arr, level):
        nonlocal max_level

        max_level = max(max_level, level)

        for node in arr:
            if type(node) == list:
                find_depth(node, level + 1)

    find_depth(nested_list, 1)

    def solve(arr, level):

        total = 0

        for node in arr:
            if type(node) == int:
                total += node * (max_level - level + 1)
            else:
                total += solve(node, level + 1)

        return total

    print(solve(nested_list, 1))


nested_list([1,[4,[6]]])'''


# Merge two binary trees
 '''def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root1 and not root2:
            return None
        if not root1:
            return root2
        if not root2:
            return root1

        root1.val=root1.val+root2.val
        root1.left=self.mergeTrees(root1.left, root2.left)
        root1.right=self.mergeTrees(root1.right, root2.right)
        return root1 '''


# Binary tree equality
'''def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right)'''


#Max path sum
'''def maxPathSum(self, root: Optional[TreeNode]) -> int:
    ans=float('-inf')

    def max_sum(root):

        nonlocal ans
        if not root:
            return 0

        ls=max(0,max_sum(root.left))
        rs=max(0,max_sum(root.right))

        ans=max(ans, root.val+ls+rs)
        return max(ls,rs)+root.val'''


#Implimentation of binary tree
'''class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


root = Tree(10)
root.left = Tree(20)
root.right = Tree(30)'''

# max continus array
            
'''def findMaxLength(self, nums: List[int]) -> int:
    ans=0
    mp={0:-1}    #(sum:pos)
    sum=0

    for i in range(len(nums)):
        if nums[i]==0:
            sum-=1
        else:
            sum+=1
        
        if sum in mp:
            ans=max(ans, i-mp[sum])         #window size =cur idx- prev occcurence index
        else:
            mp[sum]=i
        
    return ans'''

#print Binary Tree
'''
def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
    def height(root):
            nonlocal n
            
            if not root:
                return 0
            l=height(root.left)
            r=height(root.right)
            return max(l,r)+1
        
        n=height(root)
        col=pow(2,n)-1
    
        ans=[[""]*(col) for _ in range(n)]

        def fun(root,i,j,h):
            if not root:
                return 
            
            ans[i][j]=str(root.val)
            
            offset=2**(h-2) if h>1 else 0
            fun(root.left,i+1, j-offset, h-1)
            fun(root.right, i+1,j+offset, h-1)
        
        fun(root,0, col//2, n)
        return ans'''


#Max contiguous sub-sequence
'''
def max_continious(arr):
    
    temp=set()
    ans=0
    
    for ar in arr:
        temp.add(ar)
    
        
    for ar in arr:
        if (ar-1) not in temp:
            start=ar
            count=1
            while (start+1) in temp:
                count+=1
                start=start+1
            ans=max(count,ans)
    
        
    return ans
    
print(max_continious([2, 6, 1, 9, 4, 5, 3]))'''


#Edit Distance
'''def minDistance(self, word1: str, word2: str) -> int:
        
        n, m = len(word1), len(word2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = i

        for j in range(m + 1):
            dp[0][j] = j

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],      # delete
                        dp[i][j - 1],      # insert
                        dp[i - 1][j - 1]   # replace
                    )

        return dp[n][m]'''

#149 Max poins
'''class Solution(object):
    def maxPoints(self, points):
      
      ans=1
      for i in range(len(points)):
        p1=points[i]
        count=defaultdict(int)
        for j in range(i+1, len(points)):
            p2=points[j]

            if p1[0]==p2[0]:
                slope=float('inf')
            else:
                slope=(p2[1]-p1[1])/(p2[0]-p1[0])
            count[slope]+=1
            ans=max(ans, count[slope]+1)
        return ans'''

#127 Word Ladder
'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordSet=set(wordList)
        if endWord not in wordList:
            return 0

        queue=deque([(beginWord,1)])

        while queue:
            word, level=queue.popleft()

            if word==endWord:
                return level
            
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    new_word= word[:i]+ ch + word[i+1:]  

                    if new_word in wordSet:
                        queue.append((new_word , level+1))
                        wordSet.remove(new_word)
            
        return 0'''
        
