#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   368.Largest-Divisible-Subset.py
@Time    :   2020/07/05 22:33:34
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        :desc
            给出一个由无重复的正整数组成的集合，找出其中最大的整除子集，子集中任意一对 (Si，Sj) 都要满足：Si % Sj = 0 或 Sj % Si = 0。
            如果有多个目标子集，返回其中任何一个均可
        :way
对于已经排序后的nums
设定状态: dp[i]: 以nums[i]结尾的序列最大长度
last[i]: 在最大序列中 nums[i]的上一个元素在nums出现的下标
状态转移方程：
使用二重循环,对于每一个nums[i]，看他可以接在之前的哪个序列dp[j]上，使得dp[i]最长
nums[i]%nums[j] == 0是可以接的条件，dp[i]<=dp[j]是使得dp[i]变长的条件
初始状态：dp[i] = 1 (i:1 - n) 每一个只有自己的序列长度为1
        """
        dp = [1 for i in range(len(nums) + 1)]
        last =  [-1 for i in range(len(nums) + 1)]
        nums.sort()
        res_max = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] <= dp[j]:
                    dp[i] = dp[j] + 1
                    last[i] = j
            if dp[i] > res_max:
                end = i
                res_max = dp[i]
            
        idx = end
        res = []
        while idx > -1:
            res.append(nums[idx])
            idx = last[idx]
        return res

sol = Solution()
nums = [1,2,4,8, 10]
print sol.largestDivisibleSubset(nums)