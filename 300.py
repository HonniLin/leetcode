#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   300.py
@Time    :   2020/04/05 14:17:48
@Author  :   linhong02
@Desc    :   最长递增子串
O(n平方)：dp[i] 表示以 nums[i] 为结尾的最长递增子串的长度，对于每一个 nums[i]，从第一个数再搜索到i，
如果发现某个数小于 nums[i]，更新 dp[i]，更新方法为 dp[i] = max(dp[i], dp[j] + 1)，
即比较当前 dp[i] 的值和那个小于 num[i] 的数的 dp 值加1的大小，就这样不断的更新 dp 数组，到最后 dp 数组中最大的值就是我们要返回的 LIS 的长度
O(logN)：二分
"""

import bisect
class Solution(object):
    
    def lengthOfLIS_0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1 for i in range(len(nums))]
        res = 0
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        #if len(nums) == 1:
        #    return 1
        tails, res = [-float("inf")] * (len(nums)+1), 0
        for num in nums:
            i, j = 0, res
            loc = bisect.bisect_left(tails[:res + 1], num)
            tails[loc] = num
            res = max(res, loc)
            #print tails
        return res
        """
            while i < j:
                m = (i + j) // 2
                if tails[m] < num: i = m + 1 # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else: j = m
            tails[i] = num
            if j == res: res += 1
        return res
        """

sol = Solution()
nums = [10,9,2,5,3,7,101,18]
#nums = [-2, -1]
nums = [0]
print sol.lengthOfLIS(nums)