#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   87.py
@Time    :   2020/03/03 22:05:50
@Author  :   linhong02
@Desc    :   递归，遍历划分左右子树的地方
"""

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        N = len(s1)
        if N == 0:
            return True
        if N == 1:
            return s1 == s2
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1, N):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False

