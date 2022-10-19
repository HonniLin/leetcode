#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   498.py
@Time    :   2020/04/21 22:06:25
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == [] or matrix == [[]]:
            return [] 
        row_len = len(matrix)
        col_len = len(matrix[0])
        res = []
        num_sum = row_len * col_len
        i, j = 0, 0
        up = True
        while num_sum:
            num_sum -= 1
            res.append(matrix[i][j])
            if up:
                if j == col_len - 1:
                    i += 1
                    up = False
                elif i == 0:
                    j += 1
                    up = False
                else:
                    i -= 1
                    j += 1
            else:
                if i == row_len - 1:
                    up = True
                    j += 1
                elif j == 0:
                    i += 1
                    up = True
                else:
                    i += 1
                    j -= 1
        return res

sol = Solution()
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print sol.findDiagonalOrder(matrix)
            
