#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   191.py
@Time    :   2020/04/16 22:58:05
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n > 0:
            if n % 2:
                cnt = cnt + 1
            n = n >> 1
        return cnt