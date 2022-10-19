#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   120.py
@Time    :   2020/03/15 16:43:42
@Author  :   linhong02
@Desc    :   DP：把金字塔倒过来,这个时候就更加清晰了，利用动态规划的思想，
             每一个值都加上其下一层（以原来正金字塔来说）的正下方和左下方的较小值，然后不断迭代上去。
[     
[4,1,8,3],
[6,5,7],
[3,4],
[2]
]
"""

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = triangle[-1]
        for layer in range(n - 2, -1, -1):
            for i in range(layer + 1):
                dp[i] = min(dp[i], dp[i + 1]) + triangle[layer][i]
        return dp[0]

sol = Solution()
triangle = \
[ \
[2],\
[3,4], \
[6,5,7], \
[4,1,8,3] \
]
triangle = []
print sol.minimumTotal(triangle)

        