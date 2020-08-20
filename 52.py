'''
@Author: your name
@Date: 2019-11-06 21:27:39
@LastEditTime: 2019-11-06 21:43:59
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/52.py
'''
class Solution(object):
    res = 0
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        #res = 0
        def check(k, j):
            for i in range(k):
                if board[i] == j or abs(board[i] - j) == abs(k - i):
                    return False
            return True
        
        def dfs(depth):
            #nonlocal res 
            if depth == n:
                #print valuel
                self.res = self.res + 1
                return
            for i in range(n):
                if check(depth, i):
                    board[depth] = i
                    s = '.' * n
                    dfs(depth + 1)
       
        board = [-1 for i in range(n)]
        dfs(0)
        return self.res

if __name__ == "__main__":
    sol = Solution()
    print sol.totalNQueens(4)