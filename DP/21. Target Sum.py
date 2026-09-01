// Bruite Force

    def isSubsetSum(self, arr, target):
     temp=[0]
     for ar in arr:
        z=temp.copy()

        for itr in z:
            cal=itr+ar
            if cal ==target:
             return True

            temp.append(ar+itr)

     return False


# Dp sol
target = 11

sum:  0    1    2    3    4    5    6    7    8    9    10   11
dp:   T    F    F    F    F    F    F    F    F    F    F    F


class Solution:
    def isSubsetSum(self, arr, target):
        dp = [False] * (target + 1)
        dp[0] = True

        for num in arr:
            for s in range(target, num - 1, -1):

                if dp[s - num]:
                    dp[s] = True

                if dp[target]:
                    return True

        return dp[target]

        temp.append(cal)
