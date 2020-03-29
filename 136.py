#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   136.py
@Time    :   2020/03/29 18:03:20
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in nums:
            ans ^= nums[i]
        return ans