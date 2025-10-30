# https://leetcode.com/problems/check-knight-tour-configuration/description/








class Solution(object):
    def checkValidGrid(self, grid):
        dx=[2,2,-2,-2,1,1,-1,-1]
        dy=[1,-1,-1,1,2,-2,2,-2]
        n=len(grid)
        moveX,moveY=0,0
        X,Y=0,0

        if grid[0][0]!=0:
            return False

        for step in range(1,n*n):
            flag=False
            for i in range(8):
                moveX=X+dx[i]
                moveY=Y+dy[i]

                if moveX>=0 and moveY>=0 and moveX<n and moveY<n and grid[moveX][moveY]==step:
                    flag=True
                    X=moveX
                    Y=moveY
                    break
            if not flag:
                return False            
           
        return True
        
