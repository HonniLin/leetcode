#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   209.py
@Time    :   2020/04/01 08:41:49
@Author  :   linhong02
@Desc    :   求最短子序列大小 >= sum
w1：两个指针滑动
w1：二分 对前缀和进行二分
"""
import sys
import bisect
class Solution(object):
    """
    def minSubArrayLen(self, s, nums):
        
        :type s: int
        :type nums: List[int]
        :rtype: int
        
        if not nums:
            return 0
        x, y = 0, 0
        cnt = sys.maxsize
        sum = 0
        length = len(nums)
        while y < length:
            sum += nums[y]
            y += 1
            while sum >= s:
                cnt = min(cnt, y - x)
                sum -= nums[x]
                x += 1
        return 0 if cnt == sys.maxsize else cnt 
    """
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums : return 0
        # 求前缀和
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        #print(nums)
        # 总和都小于 s 时候
        if nums[-1] < s: return 0
        res = float("inf")
        nums = [0] + nums
        for i in range(1, len(nums)):
            if nums[i] - s >= 0:
                # 二分查找
                loc = bisect.bisect_left(nums, nums[i] - s)
                print i, loc
                if nums[i] - nums[loc] >= s:
                    res = min(res, i - loc)
                    continue
                if loc > 0:
                    res = min(res, i - loc + 1)
        return res 

sol = Solution()
s = 7
nums = [2,3,1,2,4,3]
print sol.minSubArrayLen(s, nums)
