#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   370.py
@Time    :   2020/03/24 08:41:57
@Author  :   linhong02
@Desc    :   区间加法
前缀和
"""

class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0 for i in range(length + 1)]
        for update in updates:
            start, end, inc = update[0], update[1], update[2]
            res[start] += inc
            res[end + 1] -= inc
        for i in range(1, length):
            res[i] += res[i - 1]
        return res[:-1]
sol = Solution()
length = 5
updates = [[1,3,2],[2,4,3],[0,2,-2]]
print sol.getModifiedArray(length, updates)

