#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   219.Contains-Duplicate-II.py
@Time    :   2020/07/02 22:03:36
@Author  :   linhong02
@Desc    :   
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。
链接：https://leetcode-cn.com/problems/contains-duplicate-ii


"""
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False