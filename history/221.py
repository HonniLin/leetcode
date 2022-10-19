#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   221.py
@Time    :   2020/03/30 21:51:00
@Author  :   linhong02
@Desc    :   在包含 0，1 的矩阵中查找只包含1的最大的正方形面积
dp：当前1格子能否组成正方形取决于上左斜上格子的数量，取最小的矩阵数。
https://www.cnblogs.com/thoupin/p/4780352.html
"""

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        row = len(matrix)
        col = len(matrix[0]) 
        dp = [[0 for i in range(col + 1)] for j in range(row + 1)]
        res = 0
        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = 1
                    if dp[i - 1][j] and dp[i][j - 1] and dp[i - 1][j - 1]: 
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                #print i, j, matrix[i - 1][j - 1], dp[i][j]
                res = max(res, dp[i][j] * dp[i][j])
        return res

sol = Solution()
matrix = [
['1','0','1','0','0'],
['1','0','1','1','1'],
['1','0','1','1','1'],
['1','0','1','1','1']
]
#matrix = [
#    ["1","0","1","0","0"],
#    ["1","0","1","1","1"],
#    ["1","1","1","1","1"],
#    ["1","0","0","1","0"]]
matrix = []
print sol.maximalSquare(matrix)
        