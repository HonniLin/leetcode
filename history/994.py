#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   994.py
@Time    :   2020/04/06 16:46:37
@Author  :   linhong02
@Desc    :   
BFS 可以看成是层序遍历。从某个结点出发，BFS 首先遍历到距离为 1 的结点，然后是距离为 2、3、4…… 的结点。
因此，BFS 可以用来求最短路径问题。BFS 先搜索到的结点，一定是距离最近的结点。
再看看这道题的题目要求：返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。
翻译一下，实际上就是求腐烂橘子到所有新鲜橘子的最短路径。那么这道题使用 BFS，应该是毫无疑问的了。

"""

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col, time = len(grid), len(grid[0]), 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = []
        # add the rotten orange to the queue
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j, time))
        # bfs
        while queue:
            i, j, time = queue.pop(0)
            for di, dj in directions:
                if 0 <= i + di < row and 0 <= j + dj < col and grid[i + di][j + dj] == 1:
                    grid[i + di][j + dj] = 2
                    queue.append((i + di, j + dj, time + 1))
        # if there are still fresh oranges, return -1
        for row in grid:
            if 1 in row: return -1

        return time

sol =Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
#grid = [[2,1,1],[0,1,1],[1,0,1]]
#grid = [[0,2]]
#grid = [[1,2,1,1,2,1,1]]
grid = [[2],[1],[1],[1],[2],[1],[1]]
print sol.orangesRotting(grid)
        