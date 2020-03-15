#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   122.py
@Time    :   2020/03/15 18:06:07
@Author  :   linhong02
@Desc    :   贪心
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == None or len(prices) < 2:
            return 0
        res = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                res = res + (prices[i + 1] - prices[i])
        
        return res

sol = Solution()
prices = [1,2,3,4,5]
print sol.maxProfit(prices)

