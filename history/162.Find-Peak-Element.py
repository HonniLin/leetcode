#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   162.Find-Peak-Element.py
@Time    :   2020/07/03 17:05:24
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :desc
            查找一个数组的峰值的index，nums = [1,2,3,1] 峰值为3 index=2
        :way
            二分
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left

sol = Solution()
nums = [1, 2, 3, 0]
print sol.findPeakElement(nums)
        