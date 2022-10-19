'''
@Author: your name
@Date: 2020-02-11 20:45:06
@LastEditTime : 2020-02-11 21:05:37
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/89.py
格雷码 https://zhuanlan.zhihu.com/p/29254973
'''
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = list()
        for i in range(1<<n):
            num = (i >> 1) ^ i
            print i, i >> 1, num
            res.append(num)
        return res

sol = Solution()
n = 3
print sol.grayCode(n)
