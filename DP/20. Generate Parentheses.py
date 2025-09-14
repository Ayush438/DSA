#  https://leetcode.com/problems/generate-parentheses/description/?envType=problem-list-v2&envId=dynamic-programming

    def generateParenthesis(self, n):
        ans=set(["()"])

        for _ in range(2,n+1):
            tempSet=set()

            for i in ans:
                for j in range(len(i)):
                    tempSet.add(i[:j]+ "()" +i[j:])
            ans=tempSet

        return list(ans)
