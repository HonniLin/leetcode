'''
@Description: 36. Valid Sudoku
@Author: linhong
@Date: 2019-10-16 21:07:17
@LastEditTime: 2019-10-16 22:24:39
@LastEditors: 
暴力求解
'''
class Solution(object):
    def isValidSudoku(self, board):
        row = [[] for _ in xrange(9)]
        col = [[] for _ in xrange(9)]
        area = [[] for _ in xrange(9)]
        for i in xrange(9):
            for j in xrange(9):
                element = board[i][j]
                if element != '.':
                    # calculate every sub-boxes, map to the left top element
                    area_left_top_id = i / 3 * 3 + j / 3
                    if element in row[i] or element in col[j] or element in area[area_left_top_id]:
                        return False
                    else:
                        row[i].append(element)
                        col[j].append(element)
                        area[area_left_top_id].append(element)
        return True