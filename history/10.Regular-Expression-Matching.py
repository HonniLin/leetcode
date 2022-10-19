#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   10.Regular-Expression-Matching.py
@Time    :   2020/07/04 18:15:10
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        :desc 
            给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
            '.' 匹配任意单个字符
            '*' 匹配零个或多个前面的那一个元素
        :way
            dp[i][j] 表示 s 的前 i 个字符与 p 中的前 j 个字符是否能够匹配
            ! 字母 + 星号的组合在匹配的过程中，本质上只会有两种情况：
                匹配 ss 末尾的一个字符，将该字符扔掉，而该组合还可以继续进行匹配；
                不匹配字符，将该组合扔掉，不再进行匹配。
        """
        dp = [ [False for i in range(len(p)+1)] for j in range(len(s)+1) ]
        dp[0][0] = True
        for i in range(1, len(p)+1):
            if p[i-1] == '*': 
                if i >= 2:
                    dp[0][i] = dp[0][i-2]
                    
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else:
                    dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]
        return dp[len(s)][len(p)]
                
        