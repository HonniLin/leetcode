#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1143.Longest-Common-Subsequence.py
@Time    :   2020/08/04 08:41:31
@Author  :   linhong02
@Desc    :   None
"""
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        :desc 最长公共子序列 不连续
        """
        m, n = len(text1), len(text2)
        # 构建 DP table 和 base case
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 进行状态转移
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # 找到一个 lcs 中的字符
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

    def LCstring(string1, string2):
        """
        最长公共子串 连续
        """
        len1 = len(string1)
        len2 = len(string2)
        res = [[0 for i in range(len1+1)] for j in range(len2+1)]
        result = 0
        for i in range(1,len2+1):
            for j in range(1,len1+1):
                if string2[i-1] == string1[j-1]:
                    res[i][j] = res[i-1][j-1]+1
                    result = max(result,res[i][j])  
    return result
