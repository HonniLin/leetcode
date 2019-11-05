'''
@Author: your name
@Date: 2019-11-05 22:14:00
@LastEditTime: 2019-11-05 23:36:40
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/51.py
回溯
'''
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def check(k, j):
            for i in range(k):
                if board[i] == j or abs(board[i] - j) == abs(k - i):
                    return False
            return True
        
        def dfs(depth, valuel):
            if depth == n:
                #print valuel
                res.append(valuel)
                return
            for i in range(n):
                if check(depth, i):
                    board[depth] = i
                    s = '.' * n
                    dfs(depth + 1, valuel + [s[:i] + 'Q' + s[i+1:]])
        res = []
        board = [-1 for i in range(n)]
        dfs(0, [])
        return res


if __name__ == "__main__":
    sol = Solution()
    print sol.solveNQueens(4)