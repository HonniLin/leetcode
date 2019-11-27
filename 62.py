'''
@Author: your name
@Date: 2019-11-26 20:51:05
@LastEditTime: 2019-11-26 20:59:23
@LastEditors: Please set LastEditors
@Description: 
@FilePath: /leetcode/62.py
'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        dp[1][1] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        
        return dp[m][n]

if __name__ == "__main__":
    sol = Solution()
    print sol.uniquePaths(7, 3) 