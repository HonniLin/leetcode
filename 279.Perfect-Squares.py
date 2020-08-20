#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   279.Perfect-Squares.py
@Time    :   2020/07/07 20:55:40
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        :desc 四平方和定理：任意一个正整数均可表示为4个整数的平方和，其实是可以表示为4个以内的平方数之和
        题目求 n 由几个平方数组成
        :way dp[i] 表示正整数i能少能由多个完全平方数组成
            建立一个长度为 n+1 的一维dp数组，将第一个值初始化为0，其余值都初始化为 INT_MAX, i从0循环到n，j从1循环到 i+j*j <= n 的位置，
            然后每次更新 dp[i+j*j] 的值，动态更新 dp 数组
        """
        dp = [float("inf") for _ in range(n + 1)]
        dp[0] = 0
        for i in range(0, n + 1):
            j = 1
            while i + j * j <= n:
                dp[i + j * j] = min(dp[i] + 1, dp[i + j * j])
                j += 1
        return dp[n]
sol = Solution()
print sol.numSquares(13)