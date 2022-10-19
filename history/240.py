#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   240.py
@Time    :   2020/03/21 23:24:51
@Author  :   linhong02
@Desc    :   行和列的数字都有序，找某个数是否存在
            从左下角或者右上角开始找。  
"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        r, c = 0, cols - 1
        while True:
            if r < rows and  c >= 0:
                if matrix[r][c] == target:
                    return True
                elif matrix[r][c] < target:
                    r += 1
                else:
                    c -= 1
            else:
                return False
sol = Solution()
matrix = [ \
  [1,   4,  7, 11, 15], \
  [2,   5,  8, 12, 19], \
  [3,   6,  9, 16, 22], \
  [10, 13, 14, 17, 24], \
  [18, 21, 23, 26, 30] \
]
print sol.searchMatrix(matrix, 20)