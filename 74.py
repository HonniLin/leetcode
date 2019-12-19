# coding=utf-8
'''
@Author: linhong
@Date: 2019-12-19 20:44:09
@LastEditTime: 2019-12-19 21:56:13
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/74.py
一个矩阵中，每行的数有序，每行的第一个大于前一行的最后一个。在矩阵中查找某个数是否存在
写了一个钟的二分 5555
另一种做法：二维数组变成一维的
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        firstrow = 0
        lastrow = len(matrix) - 1
        #print lastrow
        if lastrow < 0:
            return False
        if isinstance(matrix[0], int):
            return (target in matrix)
        else:
            left, right = 0, len(matrix[0]) - 1
        while firstrow <= lastrow:
            midrow = firstrow + (lastrow - firstrow) / 2
            #print "*******", midrow, firstrow, lastrow
            if len(matrix[midrow]) == 0:
                return False
            if matrix[midrow][left] > target:
                lastrow = midrow - 1
            elif matrix[midrow][right] < target:
                firstrow = midrow + 1
            else:
                return target in matrix[midrow]
                """
                if matrix[midrow][left] == target or matrix[midrow][right] == target:
                    return True
                while left < right - 1:
                    mid = left + (right - left) / 2
                    #print "||||", mid, left, right
                    if matrix[midrow][mid] == target:
                        return True
                    else:
                        if matrix[midrow][mid] < target:
                            left = mid
                        elif matrix[midrow][mid] > target:
                            right = mid
                """
                # return False
        return False

sol = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 3
matrix = [[1]]
target = 1
#matrix = []
#target = 2
print sol.searchMatrix(matrix, target)

