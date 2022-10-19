#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   338.Counting-Bits.py
@Time    :   2020/07/05 21:08:52
@Author  :   linhong02
@Desc    :   None
"""
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        :desc 
            给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
        :way
            奇数：二进制表示中，奇数一定比前面那个偶数多一个 1，因为多的就是最低位的 1。
            偶数：二进制表示中，偶数中 1 的个数一定和除以 2 之后的那个数一样多。因为最低位是 0，除以 2 就是右移一位，也就是把那个 0 抹掉而已，所以 1 的个数是不变的。
        """
        res = [0 for i in range(num + 1)]
        for i in range(1, num + 1):
            if i % 2 == 1:
                res[i] = res[i - 1] + 1
            elif i % 2 == 0:
                res[i] = res[i / 2]
        return res

sol = Solution()
print sol.countBits(5)
