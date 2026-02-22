class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=set()
        ans=0
        n=len(isConnected)

        def dfs(city):
            for j in range(n):
                if isConnected[city][j]==1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        for i in range(n):
            if i not in visited:
                visited.add(i)
                ans+=1
                dfs(i)
        
        return ans
