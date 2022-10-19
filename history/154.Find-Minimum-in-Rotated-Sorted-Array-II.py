#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   154.Find-Minimum-in-Rotated-Sorted-Array-II.py
@Time    :   2020/07/03 00:12:57
@Author  :   linhong02
@Desc    :   None
"""
class Solution:
    def findMin(self, nums):
        """
        :type: nums: List[int]
        :rtype: int
        :desc:
            假设按照升序排序的数组在预先未知的某个点上进行了旋转。有重复数字[2,2,2,0,1]
            ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
            请找出其中最小的元素
        :way:
            二分
        """
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) / 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]
sol = Solution()
nums = [2,2,2,0,1]
print sol.findMin(nums)