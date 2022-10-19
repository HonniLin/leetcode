#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   347.py
@Time    :   2020/04/05 15:40:55
@Author  :   linhong02
@Desc    :   
𝑂(𝑛log𝑛): sort
O(n): 桶排
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_map = dict()
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        freq_map_sort = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(freq_map_sort[i][0])
        return res

sol = Solution()
nums = [1,1,1,2,3,2]
k = 2
print sol.topKFrequent(nums, k)