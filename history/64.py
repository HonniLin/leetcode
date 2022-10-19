'''
@Author: your name
@Date: 2019-11-28 21:10:32
@LastEditTime: 2019-11-28 21:30:38
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/64.py
desc:
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0xFFFFFF for i in range(n + 1)] for j in range(m + 1)]
        for i in range(1, 1 + m):
            for j in range(1, 1 + n):
                if i == 1 and j == 1:
                    dp[i][j] = grid[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i - 1][j - 1]
            
        return dp[m][n]

if __name__ == "__main__":
    grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
    sol = Solution()
    print sol.minPathSum(grid)