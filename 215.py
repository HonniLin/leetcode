#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   215.py
@Time    :   2020/03/29 16:10:49
@Author  :   linhong02
@Desc    :   求数组中第k大的值
"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # way1: 堆
        # return heapq.nlargest(k, nums)[-1]

        # way2: 快排
        def select(nums, k):
            if len(nums) == 1:
                return nums[0]
            x = nums[0]
            i = 1
            j = len(nums) - 1
            while i < j:
                while i < j and nums[i] >= x: i += 1
                while i < j and nums[j] <= x: j -= 1
                if i == j:
                    break
                nums[i], nums[j] = nums[j], nums[i]
            if nums[i] >= x:
                nums[0], num[i] = nums[i], nums[0]
            else:
                nums[0], nums[i-1] = nums[i-1], nums[0]
                i -= 1
            if i == k - 1:
                return nums[i]
            elif k > i:
                return select(nums[i+1:], k - i - 1)
            else:
                return select(nums[:i], k)

        return select(nums, k)

sol = Solution()
nums = [3,2,1,5,6,4]
k = 2
print sol.findKthLargest(nums, k)


        