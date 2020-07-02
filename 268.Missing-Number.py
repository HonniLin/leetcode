#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   268.Missing-Number.py
@Time    :   2020/07/02 22:07:35
@Author  :   linhong02
@Desc    :   
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return (n*(n+1)/2) - sum(nums)