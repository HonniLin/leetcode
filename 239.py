#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   239.py
@Time    :   2020/04/06 18:06:51
@Author  :   linhong02
@Desc    :   双向队列
https://leetcode-cn.com/problems/sliding-window-maximum/solution/hua-dong-chuang-kou-zui-da-zhi-by-leetcode-3/
"""

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        # base cases
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        
        def clean_deque(i):
            # remove indexes of elements not from sliding window
            if deq and deq[0] == i - k:
                deq.popleft()
                
            # remove from deq indexes of all elements 
            # which are smaller than current element nums[i]
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
        
        # init deque and output
        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]
        print output
        # build output
        for i in range(k, n):
            clean_deque(i)          
            deq.append(i)
            output.append(nums[deq[0]])
            print output
        return output

sol = Solution()
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print sol.maxSlidingWindow(nums, k)