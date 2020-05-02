#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   33.py
@Time    :   2020/05/02 14:34:56
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


sol = Solution()
nums = []
target = 8
#nums = [4,5,6,7,0,1,2], target = 3
print sol.search(nums, target)