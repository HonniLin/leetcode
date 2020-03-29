#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   136.py
@Time    :   2020/03/29 18:03:20
@Author  :   linhong02
@Desc    :   求数组中只出现一次的数,其他数都出现2次
位操作的异或（^)，他的其中一个属性是，n^n = 0, 0^n = n。只要将所有的数都进行异或就得到出现一次的数。
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in nums:
            ans ^= i
        return ans