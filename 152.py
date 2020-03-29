#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   152.py
@Time    :   2020/03/29 18:07:15
@Author  :   linhong02
@Desc    :   数组中的最大乘积
为了处理负数和0，必须存储最小值和最大值
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        res = nums[0]
        ans = minn = maxn = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                maxn, minn = minn, maxn
            maxn = max(nums[i], maxn * nums[i])
            minn = min(nums[i], minn * nums[i])
            res = max(res, maxn)
        return res

sol = Solution()
nums = [2,3,-2,-4]
print sol.maxProduct(nums)