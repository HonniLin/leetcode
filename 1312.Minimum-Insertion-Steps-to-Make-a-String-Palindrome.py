#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   1312.Minimum-Insertion-Steps-to-Make-a-String-Palindrome.py
@Time    :   2020/08/03 09:10:44
@Author  :   linhong02
@Desc    :   None
"""
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        :desc 让字符串成为回文串的最少插入次数
        :way 需要在原字符串 s 中找到一个最长回文子序列，若其长度为 l，那么我们只需要添加 |s| - l 个字符，就可以将 s 变为回文串。
        时间复杂度：O(N^2)，其中 N 是字符串 s 的长度。
        空间复杂度：O(N^2)
        """
        n = len(s)
        t = s[::-1]
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n+1):
            for j in range(1, n+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                if s[i-1] == t[j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
        return n - dp[n][n]

        def minInsertions(self, s: str) -> int:
            """
            区间动态规划
            从外向内考虑 s[i:j]：
            如果 s[i] == s[j]，那么最外层已经形成了回文，我们只需要继续考虑 s[i+1:j-1]；
            如果 s[i] != s[j]，那么我们要么在 s[i:j] 的末尾添加字符 s[i]，要么在 s[i:j] 的开头添加字符 s[j]，
                才能使得最外层形成回文。如果我们选择前者，那么需要继续考虑 s[i+1:j]；如果我们选择后者，那么需要继续考虑 s[i:j-1]。
            """
            n = len(s)
            dp = [[0] * n for _ in range(n)]
            for span in range(2, n + 1):
                for i in range(n - span + 1):
                    j = i + span - 1
                    dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
                    if s[i] == s[j]:
                        dp[i][j] = min(dp[i][j], dp[i + 1][j - 1])
            return dp[0][n - 1]
    
    