#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   516.Longest-Palindromic-Subsequence.py
@Time    :   2020/08/04 08:25:46
@Author  :   linhong02
@Desc    :   None
"""
class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :desc 最长回文子序列
        """
        # 使用dp思想
        n = len(s)
        dp = [[0]*n for i in range(n)]
        # 注意basecase
        for i in range(n):
            dp[i][i] = 1
        # 倒着遍历
        for i in range(n,-1,-1):
            for j in range(i+1,n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        return dp[0][n-1]

        def longestPalindrome(self, s: str) -> str:
            """
            最长回问子串
            """
            n = len(s)
            dp = [[0] * n for _ in range(n)]
            res = ""
            for i in range(n):
                for j in range(i + 1):
                    if s[i] == s[j] and (i - j + 1 <= 3 or dp[j+1][i-1]):
                        dp[j][i] = 1
                        res = max(res, s[j:i+1], key=len)   
            return res
