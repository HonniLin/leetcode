#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   118.py
@Time    :   2020/03/15 16:03:31
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = []
        tmp = [1]
        res.append(tmp)
        if numRows == 1:
            return res
        for i in range(1, numRows):
            tmp = [1]
            for j in range(1, i):
                #print res[i-1][j]
                tmp.append(res[i-1][j] + res[i-1][j-1])
            tmp.append(1)
            res.append(tmp)
        return res

sol = Solution()
print sol.generate(5)