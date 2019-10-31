'''
@Author: your name
@Date: 2019-10-31 20:51:14
@LastEditTime: 2019-10-31 21:17:54
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/48.py
'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        
        resm = [[0 for i in range(n)] for j in range(n)]
        #print resm
        tmpi = 0
        tmpj = 0
        for j in range(0, n):
            for i in range(n-1, -1, -1):
                #print matrix[i][j]
                #print i, j, tmpi, tmpj
                resm[tmpi][tmpj] = matrix[i][j]
                tmpj = tmpj + 1
            tmpi = tmpi + 1
            tmpj = 0
        for i in range(n):
            for j range(n):
                matrix[i][j] = resm[i][j] 
        
if __name__ == "__main__":
    matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    sol = Solution()
    print sol.rotate(matrix)