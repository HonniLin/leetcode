#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   343.Integer-Break.py
@Time    :   2020/07/05 21:37:46
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        :desc
            给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
        :way
            dp[i] 能组成i的最大的乘积
        """
        dp = [0 for i in range(n + 1)]
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(j * dp[i - j], j * (i - j)))
                print j, i, dp[i]
        return dp[n]

sol = Solution()
print sol.integerBreak(8)
        
