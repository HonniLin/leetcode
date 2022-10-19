'''
@Author: your name
@Date: 2020-02-10 19:52:24
@LastEditTime : 2020-02-10 21:16:52
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/85.py
本题可以转化为84 Largest Rectangle in Histogarm来做
初始化height = [0, 0 ,0 ....]
对于每一行，先求出以这一行为x轴的每个柱子的高度，求解时，可以每次基于上一行的值进行更新。然后O(n)的时间求出最大矩形，不断更新全局变量res

作者：Jason_Yuan
链接：https://www.jianshu.com/p/cffdc94c9c19
'''
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        ret = 0
        if not matrix:
            return res

        height = [0 for i in range(len(matrix[0]))]
        for row in matrix:
            for i in range(len(row)):
                if row[i] == '0':
                    height[i] = 0
                else:
                    height[i] += 1
            ret = max(ret, self.lastRowMaxArea(height))
        
        return ret

    def lastRowMaxArea(self, height):
        if not height:
            return 0
        res = 0
        stack = []
        height.append(-1)
        for i in range(len(height)):
            cur = height[i]
            while len(stack) > 0 and cur <= height[stack[-1]]:
                h = height[stack.pop()]
                w = i if len(stack) == 0 else i - stack[-1] - 1
                res = max(res, w * h)
            stack.append(i)
        return res

sol = Solution()
matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","0","1"],
  ["1","0","0","1","0"]
]
print sol.maximalRectangle(matrix)