#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   303.Range-Sum-Query-Immutable.py
@Time    :   2020/07/07 21:13:02
@Author  :   linhong02
@Desc    :   None
"""

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.dp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            self.dp[i] = self.dp[i - 1] + nums[i - 1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j + 1] - self.dp[i]


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
param_1 = obj.sumRange(2, 5)
print param_1


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)