#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   153.Find-Minimum-in-Rotated-Sorted-Array.py
@Time    :   2020/07/02 23:47:45
@Author  :   linhong02
@Desc    :   None
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :desc:
            假设按照升序排序的数组在预先未知的某个点上进行了旋转。  
            ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
            请找出其中最小的元素。
        :way
            二分
            我们需要找到这个点。下面是关于变化点的特点：
                所有变化点左侧元素 > 数组第一个元素
                所有变化点右侧元素 < 数组第一个元素
        """
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1

        if nums[right] > nums[0]:
            return nums[0]

        res_min = nums[0]
        while left <= right:
            mid = left + (right - left) / 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[left] == nums[mid]:
                left += 1
            elif nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1

sol = Solution()
nums = [3,4,5,1,2]
print sol.findMin(nums)