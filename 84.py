# coding=gbk
'''
@Author: your name
@Date: 2020-01-14 20:20:22
@LastEditTime : 2020-01-14 21:26:00
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: /undefined/Users/linhong02/Documents/meme/code/leetcode/84.py
'''
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        long = len(heights)
        res = 0
        for i in range(long):
            # һ���Ż� ����ǰ�Ⱥ�һ����ʱ������Ҫ����
            if i + 1 < long and heights[i] <= heights[i + 1]:
                continue
            #�ҵ�һ���ֲ���ֵ����ǰ��������
            cntmin = heights[i]
            for j in range(i, -1, -1):
                if cntmin > heights[j]:
                    cntmin = heights[j]
                res = max(res, (i - j + 1) * cntmin)
        
        return res

sol = Solution()
heights = [2,1,5,6,2,3]
heights = [1]
print sol.largestRectangleArea(heights)
                
