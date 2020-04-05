#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   415.py
@Time    :   2020/04/05 16:00:07
@Author  :   linhong02
@Desc    :   大数相加：关键：res = str(tmp % 10) + res
"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = ""
        i, j, cnt = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + cnt
            cnt = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return  "1" + res if cnt else res

sol = Solution()
num1 = "55"
num2 = "66"
print sol.addStrings(num1, num2)