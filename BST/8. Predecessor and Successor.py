
class Solution:
    def findPreSuc(self, root, key):
        
        pre=suc=None
        cur=root
        
        while cur:
            
            if cur.data==key:
                # presossor
                temp=cur.left
                while temp and temp.right:
                    temp=temp.right
                  
                if temp:
                    pre=temp
                    
                #Succsessor
                temp=cur.right
                while temp and temp.left:
                    temp=temp.left
                
                if temp:
                    suc=temp
                break
                    
            elif cur.data>key:
                suc=cur
                cur=cur.left
            
            else:
                pre=cur
                cur=cur.right
            
        return [pre, suc]
