"""
https://www.cnblogs.com/grandyang/p/4299608.html
卡塔兰数 Catalan Numbe
"""
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]

sol = Solution()
print sol.numTrees(3)