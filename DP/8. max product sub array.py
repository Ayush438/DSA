#  https://leetcode.com/problems/maximum-product-subarray/description/

#Ques=  find the contigius subarray with max product

#  arr=[  2  3  -2  -5   6  -1  4]
#  start from left  |  start from right  |  max profit            #one edge case if get 0 anywhere instead of writing 0 write it as 1
#      2            |    4               |  4                     # So values after the zero will not become 0
#    2*3= 6         |   -4               |  6
#    6*-2=-12       |  -24               |  6
#   -12* -5=60      |  120               |  120
#   60*6  =360      |  -240              |  360
#   360*-1= -360    |  -720              |  360
#   -360*4=-1440    |  -1440             |  360

 def maxProduct(self, nums):
       
       left_product=1
       right_product=1
       max_product=nums[0]
       n=len(nums)
       
       for i in range(n):
         left_product = left_product * nums[i] if left_product != 0 else nums[i]
         right_product = right_product * nums[n-i-1] if right_product != 0 else nums[n-i-1]
         max_product=max(max_product,left_product,right_product)

       return max_product
