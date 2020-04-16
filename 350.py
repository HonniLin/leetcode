#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   350.py
@Time    :   2020/04/16 22:56:39
@Author  :   linhong02
@Desc    :   先排序，再用指针遍历
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        ans = []
        left, right = 0, 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] < nums2[right]:
                left = left + 1
            elif nums1[left] > nums2[right]:
                right = right + 1
            else:
                ans.append(nums1[left])
                left = left + 1
                right = right + 1
        return ans