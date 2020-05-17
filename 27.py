#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   27.py
@Time    :   2020/05/17 13:19:36
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

sol = Solution()
nums = [2, 3, 3, 4]
val = 3
print sol.removeElement(nums, val)