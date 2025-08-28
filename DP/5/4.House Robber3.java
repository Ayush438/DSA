// https://leetcode.com/problems/house-robber-iii/description/

        3 (root)                    1
       / \                         / \
      2   3                       9    2
         / \                     /     / \
        3   1                   3     8   7

  max=3+3+1=7                  max=9+8+7=24
                                                            
                                    1 (root)                 [1+3+15=19,  Max(a,b)=9+15=24]    #if take 1 we can not take 9 and 2
                                                                                               #if not then max(left, right)
                                   / \                      
                                  9   2                  a= [9 , 3]       b=   [2 , 15]      #if takes2 we can not take either 8 or 7
                                 /   / \                                                     #similarly if i take 9 i can not take 3
          
                                3   8   7               [3 , 0]          [8 , 0]      [7 , 0]----------------[take, Not take]


      A            [skip(B)+skip(C),  Max( rob(B), skip(B))+ Max( rob(C), skip(C))]
    /    \
  B        C      


    
class Solution(object):
    def robber(self, root):
        if root==None:
            return [0,0]

        left=self.robber(root.left)
        right=self.robber(root.right)

        rob=root.val+left[1]+right[1]
        not_rob=max(left[0],left[1])+max(right[0],right[1])

        return [rob,not_rob]

    def rob(self, root):
        temp=self.robber(root)
        return max(temp[0],temp[1])

    
