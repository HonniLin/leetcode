#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   121.py
@Time    :   2020/03/15 17:52:19
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == None or prices == []:
            return 0

        min_price = prices[0]
        res = 0
        for i in range(len(prices)):
            res = max(res, prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return res

sol = Solution()
prices = [7,1,5,3,6,4]
print sol.maxProfit(prices)