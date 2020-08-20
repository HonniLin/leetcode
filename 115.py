#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   115.py
@Time    :   2020/03/14 13:45:55
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [ [0 for i in range(len(s) + 1)] for j in range(len(t) + 1) ]
        for i in range(len(s) + 1):
            dp[i][0] = 1
        for i in range(1, len(s) + 1):
            for j in range(1, len(t) + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(s)][len(t)]

sol = Solution()
s = "rabbbit"
t = "rabbit"
print sol.numDistinct(s, t)