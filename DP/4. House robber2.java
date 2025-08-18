// https://leetcode.com/problems/house-robber-ii/description/

class Solution {
    public int rob(int[] nums) {
        
        int n=nums.length;

        if(n==1) return nums[0];
        if(n==2) return Math.max(nums[0],nums[1]);

        int skipFirst[]=new int[n-1];        //Dont take First element because of loop
        int skipLast[]=new int[n-1];        //Dont take Last element because of loop

        for(int i=0;i<n-1;i++)
        {
            skipLast[i]=nums[i];
            skipFirst[i]=nums[i+1];
        }

        int lootSkipLast=robber(skipLast);
        int lootSkipFirst=robber(skipFirst); 

        return Math.max(lootSkipLast, lootSkipFirst);
    }

    public int robber(int arr[])
    {
        int n=arr.length;
        int temp[]=new int[n+1];

        temp[0]=arr[0];
        temp[1]=Math.max(arr[0],arr[1]);

        for(int i=2;i<n;i++)
        {
            temp[i]=Integer.max(arr[i]+temp[i-2], temp[i-1]);
        }

        return temp[n-1];
    }
}
