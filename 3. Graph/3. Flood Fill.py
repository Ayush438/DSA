class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n,m= len(image), len(image[0])
        origional=image[sr][sc]

        if origional == color:
            return image

        def dfs(i,j):
            if i<0 or j<0 or i>=n or j>=m or image[i][j]!=origional:
                return
            
            image[i][j]=color

            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i,j+1)

        #image[sr][sc]=color
        dfs(sr, sc)
        return image
