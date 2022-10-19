#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   329.py
@Time    :   2020/03/31 21:45:37
@Author  :   linhong02
@Desc    :   求数字矩阵中的最长上升路径
matrix_map[x][y] 记录当前格子可以往后走的最长路径
"""

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        row = len(matrix)
        if row == 0:
            return 0
        col = len(matrix[0])
        if col == 0:
            return 0
        matrix_map = [[0 for i in range(col)] for j in range(row)]

        disx = [0, 0, 1, -1]
        disy = [1, -1, 0, 0]

        res = 0
        def dfs(matrix, matrix_map, x, y):
            if matrix_map[x][y] != 0:
                return matrix_map[x][y]
            maxnum = 1
            for i, j in zip(disx, disy):
                xx = x + i
                yy = y + j
                if xx >= 0 and xx < row and yy >= 0 and yy < col and \
                   matrix[x][y] < matrix[xx][yy]:
                    maxnum = max(maxnum, dfs(matrix, matrix_map, xx, yy) + 1)
            matrix_map[x][y] = maxnum
            return maxnum
                    
        for i in range(row):
            for j in range(col):
                if matrix_map[i][j] == 0:
                    res = max(res, dfs(matrix, matrix_map, i, j))
                    #print i, j, matrix[i][j], res 
        return res
        
sol = Solution()
matrix = [
  [9,9,4], \
  [6,6,8], \
  [2,1,1]
]
matrix = [[]]
print sol.longestIncreasingPath(matrix)