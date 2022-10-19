class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix or not matrix[0]:
            pass
        else:
            row = len(matrix)
            col = len(matrix[0])
            self.dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
            for i in range(1, row + 1):
                for j in range(1, col + 1):
                    self.dp[i][j] = self.dp[i][j - 1] + self.dp[i - 1][j] - self.dp[i - 1][j - 1] + matrix[i - 1][j - 1]


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        :desc 二维区域和的检索 是303题的衍生
        :way dp[i][j]表示累计区间(0, 0)到(i, j)这个矩形区间所有的数字之和
        """
        return self.dp[row2 + 1][col2 + 1] + self.dp[row1][col1] - self.dp[row2 + 1][col1] - self.dp[row1][col2 + 1]
        


# Your NumMatrix object will be instantiated and called as such:
matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
obj = NumMatrix(matrix)
param_1 = obj.sumRegion(2, 1, 4, 3)
print param_1