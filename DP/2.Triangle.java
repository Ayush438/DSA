//  https://leetcode.com/problems/triangle/

//     2                      9          ^
//    1  3                  10 7         |
//   8  9  1              9  10  4       |
//  4  1  8  3          4   1   8   3    |
//                    0  0   0   0   0
 public int minimumTotal(List<List<Integer>> triangle)
  {
        int n=triangle.size();
        int temp[][]=new int[n+1][n+1];

        for(int i=n-1;i>=0;i--)
        {
            for(int j=0;j<=i;j++)
            {
                temp[i][j]=triangle.get(i).get(j)+ Math.min(temp[i+1][j], temp[i+1][j+1]);
            }
        }
        return temp[0][0];
}
