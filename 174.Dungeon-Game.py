#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   174.Dungeon-Game.py
@Time    :   2020/07/06 16:02:56
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        :way
            从右下走回左上
            dp[i][j] 表示在i,j位置最少需要的血量
        """
        if dungeon is None or len(dungeon) == 0 or len(dungeon[0]) == 0:
            return 0
        
        row = len(dungeon)
        col = len(dungeon[0])

        res = 0
        dp = [[-0xffffff for _ in range(col)] for _ in range(row)]
        dp[row - 1][col - 1] = max(0, -dungeon[row - 1][col - 1])
        #要考虑边界，因为边界只有一种选择 
        #设置最后一列的值
        for i in range(row - 2, -1, -1):
            needMin = dp[i + 1][col - 1] - dungeon[i][col - 1]
            dp[i][col - 1] = max(0, needMin)
        
        # 设置最后一行的值
        for i in range(col - 2, -1, -1):
            needMin = dp[row - 1][i + 1] - dungeon[row - 1][i]
            dp[row - 1][i] = max(0, needMin)
        
        for i in range(row - 2, -1, -1):
            for j in range(col - 2, -1, -1):
                needMin = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = max(0, needMin)
        return dp[0][0] + 1
        
sol = Solution()
dungeon = [
    [-2, -3],
    [-5, 3]
]
print sol.calculateMinimumHP(dungeon)