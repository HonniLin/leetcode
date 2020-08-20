#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   31.py
@Time    :   2020/05/19 11:25:19
@Author  :   linhong02
@Desc    :   得到下一个排列
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                nums[i:] = sorted(nums[i:])
                for j in range(i, len(nums)):
                    if nums[j] > nums[i - 1]:
                        nums[j], nums[i - 1] = nums[i - 1], nums[j]
                        break
                return
        nums.sort()