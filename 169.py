#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   169.py
@Time    :   2020/04/05 16:22:14
@Author  :   linhong02
@Desc    :   
w1：字典树法
w2：摩尔投票法
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        l = len(nums)
        return nums[l/2]

sol = Solution()
nums = [2,2,1,1,1,2,2]
print sol.majorityElement(nums)