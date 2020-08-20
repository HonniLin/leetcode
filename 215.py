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

# way2: 分治
class Solution:
    def findKthLargest(self, nums, k):
        pos = self.partition(nums)
        if pos + 1 == k:
            return nums[pos]
        elif pos + 1 > k:
            return self.findKthLargest(nums[:pos], k)
        else:
            return self.findKthLargest(nums[pos+1:], k - pos - 1)
    
    def partition(self, nums):
        i = 0
        for j in range(len(nums)):
            if nums[j] > nums[-1]: #the larger elements are in left side
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[-1] = nums[-1], nums[i]
        return i

sol = Solution()
nums = [3,2,1,5,6,4]
k = 2
print sol.findKthLargest(nums, k)


        