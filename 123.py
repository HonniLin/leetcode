#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   123.py
@Time    :   2020/03/15 18:34:16
@Author  :   linhong02
@Desc    :   两次遍历。
第一次从左到右，得到从开始到第 i 天，所能获得的最大收益。
第二次从右到左，得到从第 i 天到最后一天，所能获得的最大收益。
最后，对于任意的 i (0 <= i < size)，它把数组分成两部分，这两部分的最大收益之和就是最终的收益。找出其中最大的那个。

可以把数组一切为2，[0, i] 为第一次交易， [i, prices.length - 1] 为第二次交易。
特定到i点时，可在i点把货物卖出，作为[0, i]区域的终结，然后再i点把货物买入， 作为[i, prices.length - 1]区域的开始
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        pre = []
        low = float('inf')
        res = 0
        for i in xrange(len(prices)):
            low = min(prices[i], low)
            res = max(res, prices[i] - low)
            pre.append(res)
        high = float("-inf")
        res = 0
        total_max = 0
        for i in xrange(len(prices)-1, -1, -1):
            high = max(prices[i], high)
            res = max(res, high - prices[i])
            total_max = max(total_max, pre[i] + res)
        return total_max

sol = Solution()
prices = [3,3,5,0,0,3,1,4]
print sol.maxProfit(prices)
