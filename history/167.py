#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   167.py
@Time    :   2020/03/30 22:31:34
@Author  :   linhong02
@Desc    :   None
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i + 1, j + 1]

sol = Solution()
numbers = [2,3,7,15]
target = 9
print sol.twoSum(numbers, target)

        