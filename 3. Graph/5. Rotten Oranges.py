class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m=len(grid), len(grid[0])
        fresh=ans=0
        queue=deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    queue.append((i,j))

        dir=[[1,0],[0,-1],[0,1],[-1,0]]
        
        while queue and fresh>0:
            for _ in range(len(queue)):
                x,y=queue.popleft()

                for dx,dy in dir:
                    _x=dx+x
                    _y=dy+y

                    if _x>-1 and _y>-1 and _x<n and _y<m and grid[_x][_y]==1:
                        grid[_x][_y]=2
                        queue.append((_x,_y))
                        fresh-=1
            ans+=1

        return ans if fresh==0 else -1
