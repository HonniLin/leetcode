'''
@Author: your name
@Date: 2019-11-27 21:11:37
@LastEditTime: 2019-11-27 21:40:15
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/63.py
'''
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        #print m, n
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        dp[1][1] = 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    dp[i][j] = 1
                else:
                    print i-1, j-1
                    if obstacleGrid[i-1][j-1] == 1:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        return dp[m][n]

if __name__ == "__main__":
    ob = [
  [0,0,0],
  [0,1,1],
  [0,0,0]
]
    ob = [[0,0]]
    sol = Solution()
    print sol.uniquePathsWithObstacles(ob)