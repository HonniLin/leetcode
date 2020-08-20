# coding=utf-8
'''
@Author: your name
@Date: 2020-01-06 22:35:53
@LastEditTime: 2020-01-06 23:34:34
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/79.py
递归，上下左右遍历
'''
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        hang = len(board)
        lie = len(board[0])
        nums = len(word)


        def check(ii, jj, cnt):
            if cnt == nums:
                return True
            ti = ii + 1
            tj = jj + 1
            bi = ii - 1
            bj = jj - 1
            if tj < lie:
                if board[ii][tj] == word[cnt]:
                    tmp = board[ii][tj]
                    board[ii][tj] = '#'
                    if check(ii, tj, cnt+1):
                        return True
                    board[ii][tj] = tmp 
            if ti < hang:
                if board[ti][jj] == word[cnt]:
                    tmp = board[ti][jj]
                    board[ti][jj] = '#' 
                    if check(ti, jj, cnt+1):
                        return True
                    board[ti][jj] = tmp
            if bi >= 0:
                if board[bi][jj] == word[cnt]:
                    tmp = board[bi][jj] 
                    board[bi][jj] = '#'
                    if check(bi, jj, cnt+1):
                        return True
                    board[bi][jj] = tmp
            if bj >= 0:
                if board[ii][bj] == word[cnt]:
                    tmp = board[ii][bj]
                    board[ii][bj] = '#' 
                    if check(ii, bj, cnt+1):
                        return True
                    board[ii][bj] = tmp 
            return False

        for i in range(hang):
            for j in range(lie):
                if board[i][j] == word[0]:
                    board[i][j] = '#'
                    if check(i, j, 1) == True:
                        return True
                    board[i][j] = word[0]
                    
        return False

#https://leetcode.com/problems/word-search/discuss/27660/Python-dfs-solution-with-comments.
def exist(self, board, word):
    if not board:
        return False
    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            if self.dfs(board, i, j, word):
                return True
    return False

# check whether can find word, start at (i,j) position    
def dfs(self, board, i, j, word):
    if len(word) == 0: # all the characters are checked
        return True
    if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
        return False
    tmp = board[i][j]  # first character is found, check the remaining part
    board[i][j] = "#"  # avoid visit agian 
    # check whether can find "word" along one direction
    res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
    or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
    board[i][j] = tmp
    return res

sol = Solution()
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
board = [
    ["C","A","A"],
    ["A","A","A"],
    ["B","C","D"]]

word = "ABCCED"
word = "SEE"
word = "ABCB"
word = "ABFCC"
word = "AAD"
print sol.exist(board, word)
