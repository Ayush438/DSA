#  https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/


class Solution(object):
    def findLength(self, nums1, nums2):
        n, m = len(nums1), len(nums2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = 0 
        
        return ans
