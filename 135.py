#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   135.py
@Time    :   2020/04/09 21:10:19
@Author  :   linhong02
@Desc    :   
先从左至右遍历学生成绩 ratings，按照以下规则给糖，并记录在 left 中。
同理，在此规则下从右至左遍历学生成绩并记录在 right 中，可以保证所有学生糖数量 满足右规则。
最终，取以上 22 轮遍历 left 和 right 对应学生糖果数的 最大值 ，这样则 同时满足左规则和右规则 ，即得到每个同学的最少糖果数量。
"""

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        left = [1] * len(ratings)
        right = left[:]
        cnt = 0
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        cnt = left[-1]
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
            cnt += max(left[i], right[i])
        
        return cnt

sol = Solution()
ratings = [1,3,4,5,2]
print sol.candy(ratings)