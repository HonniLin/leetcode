#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   357.Count-Numbers-with-Unique-Digits.py
@Time    :   2020/07/05 22:20:20
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        :desc 
            给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10n
        :way   
            n=1: res=10
n=2: res=9*9+10=91 # 两位数第一位只能为1-9，第二位只能为非第一位的数，加上一位数的所有结果
n=3: res=9 * 9 * 8+91=739 # 三位数第一位只能为1-9，第二位只能为非第一位的数，第三位只能为非前两位的数，加上两位数的所有结果
n=4: res=9 * 9 * 8 * 7+739=5275 # 同上推法
        """
        res, mul = 10, 9
        for i in range(1, min(n, 10)):
            mul *= 10 - i
            res += mul
        return res

sol = Solution()
print sol.countNumbersWithUniqueDigits(4)