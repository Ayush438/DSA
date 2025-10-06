class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans=0
        left=0
        n=len(s)
        temp=set()

        for right in range(n):
            while s[right] in temp:
                temp.remove(s[left])
                left+=1

            temp.add(s[right])
            ans=max(ans, right-left+1)

        return ans
