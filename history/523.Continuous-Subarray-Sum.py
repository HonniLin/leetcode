#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   523.Continuous-Subarray-Sum.py
@Time    :   2020/07/07 22:09:27
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        :desc 一个数组和一个数字k，让我们求是否存在这样的一个连续的子数组，该子数组的数组之和可以整除k
        :way 若数字a和b分别除以数字c，若得到的余数相同，那么(a-b)必定能够整除c
        注意k=0的情况
        """
        n = len(nums)
        st = set()
        sum = 0
        pre = 0
        for i in range(0, n):
            sum += nums[i]
            t = sum if k == 0 else sum % k
            if t in st:
                return True
            st.add(pre)
            pre = t
        return False

sol = Solution()
nums = [23, 2, 4, 6, 7]
k=6
print sol.checkSubarraySum(nums, k)

        