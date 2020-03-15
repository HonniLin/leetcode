#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   119.py
@Time    :   2020/03/15 16:17:24
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        row = [0, 1]
        for i in range(1, rowIndex + 1):
            tmp2 = 0
            for j in range(1, i + 1):
                tmp = row[j]
                row[j] = tmp2 + row[j]
                tmp2 = tmp
                
            row.append(1)
        
        return row[1:]

# way2:可以利用杨辉三角一个很重要的特性快速得到结果，那就是一行的数组可以有上一行的数组前后分别添加0 相加得到
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        """
            Time Complexity:O(K^2)
            Space Complexity:O(K)
        """
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row


sol = Solution()
print sol.getRow(4)
        