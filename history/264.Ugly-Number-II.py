#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   264.Ugly-Number-II.py
@Time    :   2020/07/07 20:22:40
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        :desc 查找第n个丑数 （Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.）
        :way 一个丑陋数分别乘以 2，3，5，而要求的丑陋数就是从已经生成的序列中取出来的，每次都从三个列表中取出当前最小的那个加入序列
        """
        nums = [1,]
        i2 = i3 = i5 = 0
        for i in range(1, 1690):
            ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(ugly)
            if ugly == nums[i2] * 2:
                i2 += 1
            if ugly == nums[i3] * 3:
                i3 += 1
            if ugly == nums[i5] * 5:
                i5 += 1
        return nums[n - 1]

sol = Solution()
n = 10
print sol.nthUglyNumber(n)
