'''
@Author: linhong02
@Date: 2019-12-18 21:38:13
@LastEditTime: 2019-12-18 22:07:14
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/73.py
desc:Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

方法3：（常数额外空间）
1. 找到一个零的位置，把这行这列当做方法2中的两个数组存值。
2. 根据1的位置的所在行和列的值是否有零将矩阵相应位置置零。
3. 再把1中零所在位置的行和列置零。

'''
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0]) #lie
        row = [0 for i in range(n)]
        column = [0 for i in range(m)]
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row[i] = 1
                    column[j] = 1
        
        for i in range(n):
            for j in range(m):
                if row[i] == 1 or column[j] == 1:
                    matrix[i][j] = 0
        
        return matrix
    
    def way3_setZeroes(self, matrix)
    {
        int len1 = matrix.size();
        if (len1 == 0) return ;
        int len2 = matrix[0].size();
        if (len2 == 0) return ;
        int row = -1, col = -1;
        for (int i = 0; i < len1; i++)
            for (int j = 0; j < len2; j++)
            {
                if (matrix[i][j] == 0)
                {
                    row = i; col = j;
                }
            }
        if (row == -1) return;
        for (int i = 0; i < len1; i++)
            for (int j = 0; j < len2; j++)
            {
                if (matrix[i][j] == 0 && i != row && j != col)
                {
                    matrix[i][col] = 0;
                    matrix[row][j] = 0;
                }
            }
        for (int i = 0; i < len1; i++)
            for (int j = 0; j < len2; j++)
            {
                if (i != row && j != col)
                {
                    if (matrix[i][col] == 0 )
                        matrix[i][j] = 0;
                    else if (matrix[row][j] == 0)
                        matrix[i][j] = 0;
                }
            }
        int index = -1; 
        while(++index < len1) matrix[index][col] = 0;
        index = -1;
        while(++index < len2) matrix[row][index] = 0;
        return ;
    }


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        row0_flag = False
        col0_flag = False
        # 找第一行是否有0
        for j in range(col):
            if matrix[0][j] == 0:
                row0_flag = True
                break
        # 第一列是否有0
        for i in range(row):
            if matrix[i][0] == 0:
                col0_flag = True
                break

        # 把第一行或者第一列作为 标志位
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        #print(matrix)
        # 置0
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row0_flag:
            for j in range(col):
                matrix[0][j] = 0
        if col0_flag:
            for i in range(row):
                matrix[i][0] = 0

#链接：https://leetcode-cn.com/problems/set-matrix-zeroes/solution/o1kong-jian-by-powcai/

sol = Solution()
matrix = \
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
matrix = \
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
print sol.setZeroes(matrix)