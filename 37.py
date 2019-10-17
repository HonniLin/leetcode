'''
@Description: In User Settings Edit
@Author: linhong
@Date: 2019-10-17 21:10:04
@LastEditTime: 2019-10-17 22:33:00
@LastEditors: 
dfs
遍历整个map，依次填入数据，判断这个数据是否合适。合适则继续填，不合适则回溯
'''
class Solution(object):
    def isValid(self, board, x, y):
        tmp = board[x][y]; board[x][y]='D'
        for i in range(9):
            if board[x][i] == tmp:
                return False
            if board[i][y] == tmp:
                return False
        for i in range(3):
            for j in range(3):
                if board[x/3*3+i][y/3*3+j] == tmp:
                    return False
        board[x][y]=tmp
        return True
        
    def dfs(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in '123456789':
                        board[i][j] = k
                        if self.isValid(board, i, j) and self.dfs(board):
                            return True
                        board[i][j] = '.' #回溯
                    return False
        return True

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.dfs(board)
        print board
                
if __name__ == "__main__":
    #print "***"
    print (Solution().solveSudoku([
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]))
     