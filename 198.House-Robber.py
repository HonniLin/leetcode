#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   198.House-Robber.py
@Time    :   2020/07/06 11:49:24
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :desc 
            如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
            给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
        :way: 
            用 dp[i]dp[i] 表示前 ii 间房屋能偷窃到的最高总金额
            1/偷窃第 kk 间房屋，那么就不能偷窃第 k-1k−1 间房屋，偷窃总金额为前 k-2k−2 间房屋的最高总金额与第 kk 间房屋的金额之和。
            2/不偷窃第 kk 间房屋，偷窃总金额为前 k-1k−1 间房屋的最高总金额。
        """
        if nums == None or len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[n - 1]

sol = Solution()
nums = [1,2,3,1]
print sol.rob(nums)