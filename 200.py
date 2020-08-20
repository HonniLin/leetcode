#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   200.py
@Time    :   2020/03/18 08:42:22
@Author  :   linhong02
@Desc    :   dfs 基础题
"""

class Solution(object):
    direction0 = [0, 0, 1, -1]
    direction1 = [1, -1, 0, 0]
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        :desc 岛屿数量
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j)
        return res

    def dfs(self, grid, x, y):
        grid[xx][yy] = '0'
        for i in range(4):
            xx = x + self.direction0[i]
            yy = y + self.direction1[i]
            if xx >= 0 and xx < len(grid) and yy >= 0 and yy < len(grid[0]) and grid[xx][yy] == '1':
                self.dfs(grid, xx, yy)

sol = Solution()
print sol.numIslands(grid)