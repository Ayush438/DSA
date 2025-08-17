//  https://leetcode.com/problems/house-robber/description/

// loot=[2  7  3  1  4  2  1  8]
//  Total loot at house(n)  =MAX( total_loot[n-2] + loot[n], total_loot[n-1])
//                                                |                |
//                                          select(n)            Not select

//   2  7  3  1
//[  2  7  7  8         ---total loot
//                  loot at (2)= MAX(2+3, 7)=7,    loot at (3)= MAX(7+1, 7)=8


public int rob(int[] nums)
  {      
        int n=nums.length;
        int temp[]=new int[n+1];

        if(n<2) return nums[0];

        temp[0]=nums[0];
        temp[1]=Math.max(nums[0],nums[1]);

        for(int i=2;i<n;i++)
        {
            temp[i]= Math.max(temp[i-2]+nums[i], temp[i-1]);
        }
        return temp[n-1];
    }
