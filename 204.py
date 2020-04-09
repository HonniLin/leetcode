#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   204.py
@Time    :   2020/04/09 20:40:26
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        signs = [True] * (n + 1)
        cnt = 0
        for i in range(2, n):
            if signs[i]:
                cnt += 1
            for j in range(i + i, n, i):
                signs[j] = False
        return cnt

sol = Solution()
n = 10
print sol.countPrimes(n)
        