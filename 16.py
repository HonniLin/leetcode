#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   16.py
@Time    :   2020/05/02 15:51:57
@Author  :   linhong02
@Desc    :   
先排序，固定一个数，再用两个指针去遍历，sum大于target，则right 移动；sum 小于target， 则left移动
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        leng = len(nums)
        cnt = 0xffffff
        ans = 0
        for i in range(0, leng - 2):
            left = i + 1
            right = leng - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                diff = abs(s - target)
                if diff < cnt:
                    cnt = diff
                    ans = s
                elif diff == 0:
                    return s
                if s < target:
                    left += 1
                else:
                    right -= 1
        return ans
            
        
sol = Solution()
nums = [-1, 2, 1, -4]
target = -3
print sol.threeSumClosest(nums, target)
