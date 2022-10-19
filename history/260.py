#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   260.py
@Time    :   2020/04/14 22:41:34
@Author  :   linhong02
@Desc    :   
补码(反码+1)就是负数在计算机中的二进制表示方法。
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        bitmask = 0
        for num in nums:
            bitmask ^= num
        print bin(bitmask), bin(-bitmask) 
        diffbit = bitmask & (-bitmask)
        print bin(diffbit)
        x = 0
        for num in nums:
            if num & diffbit:
                x ^= num
        return [x, bitmask ^ x]

sol = Solution()
nums = [1,2,1,3,2,5]
print sol.singleNumber(nums)