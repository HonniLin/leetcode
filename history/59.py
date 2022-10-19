'''
@Author: your name
@Date: 2019-11-19 21:32:35
@LastEditTime: 2019-11-19 22:22:36
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/59.py
题目类似 No.54
仿照遍历方法，填数字
'''
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        maxn = n * n + 1
        res = list()
        res = [[0 for i in range(n)] for j in range(n)]
        
        lm = 0
        rm = n - 1
        ln = 0
        rn = n - 1
        cnt = 1
        while lm <= rm and ln <= rn:
            for i in range(ln, rn+1):
                res[lm][i] = cnt
                cnt = cnt + 1
            for i in range(lm+1, rm+1):
                res[i][rn] = cnt
                cnt = cnt + 1
            for i in range(rn-1, ln-1, -1):
                if lm < rm:
                    res[rm][i] = cnt
                    cnt = cnt + 1
            for i in range(rm-1, lm, -1):
                if ln < rn:
                    res[i][ln] = cnt
                    cnt = cnt + 1
            lm = lm + 1
            rm = rm - 1
            ln = ln + 1
            rn = rn - 1
        
        return res
        
if __name__ == "__main__":
    sol = Solution()
    print sol.generateMatrix(4)